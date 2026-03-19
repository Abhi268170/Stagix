#!/usr/bin/env python3
"""Stop hook: Writes gate file when an agent completes.

Fires when any agent produces its final response.
Creates .stagix/gates/{stage}.pending.json with review instructions.
Sends desktop notification. Writes confluence-update-pending flag.
"""

import json
import sys
import os
import subprocess
import glob
from datetime import datetime

# Map agent names to gate stage names
AGENT_TO_STAGE = {
    "codebase-archaeologist": "discovery",
    "business-analyst": "business-analyst",
    "product-manager": "product-manager",
    "ux-designer": "ux-designer",
    "solution-architect": "solution-architect",
    "db-designer": "db-designer",
    "technical-writer": "technical-writer",
    "scrum-master": "scrum-master",
    "devops": "devops",
    "test-case-specialist": "test-plan",
    "security-specialist": "security",
    "tech-lead-reviewer": "tech-lead",
    "qa-engineer": "qa",
}

# Map stage to next agent
NEXT_AGENT = {
    "discovery": "business-analyst",
    "business-analyst": "product-manager",
    "product-manager": "ux-designer + solution-architect (parallel)",
    "ux-designer": "solution-architect (finalise)",
    "solution-architect": "db-designer",
    "db-designer": "technical-writer",
    "technical-writer": "scrum-master",
    "scrum-master": "Engineering Collective (Group 2 unlocked)",
    "devops": "test-case-specialist",
    "test-plan": "backend-dev + frontend-dev (test implementation)",
    "security": "tech-lead-reviewer",
    "tech-lead": "qa-engineer",
    "qa": "Final human approval",
}


def send_notification(title, message):
    """Send desktop notification (Linux or macOS)."""
    try:
        if sys.platform == "linux":
            subprocess.run(["notify-send", title, message], timeout=5)
        elif sys.platform == "darwin":
            subprocess.run([
                "osascript", "-e",
                f'display notification "{message}" with title "{title}"'
            ], timeout=5)
    except (FileNotFoundError, subprocess.TimeoutExpired):
        pass  # Notification not available — skip


def main():
    data = json.load(sys.stdin)
    cwd = data.get("cwd", os.getcwd())
    agent_type = data.get("agent_type", "")

    # CRITICAL: Prevent infinite loops. If stop_hook_active is true,
    # Claude is already continuing from a previous Stop hook — exit immediately.
    if data.get("stop_hook_active", False):
        sys.exit(0)

    if not agent_type or agent_type not in AGENT_TO_STAGE:
        sys.exit(0)  # Not a Stagix agent — skip

    stage = AGENT_TO_STAGE[agent_type]
    gates_dir = os.path.join(cwd, ".stagix", "gates")
    os.makedirs(gates_dir, exist_ok=True)

    # Find output files (recently modified files in .stagix/docs/)
    docs_dir = os.path.join(cwd, ".stagix", "docs")
    outputs = []
    if os.path.exists(docs_dir):
        for root, dirs, files in os.walk(docs_dir):
            for f in files:
                if f.endswith(".md"):
                    outputs.append(os.path.relpath(os.path.join(root, f), cwd))

    # Write pending gate file
    gate_file = os.path.join(gates_dir, f"{stage}.pending.json")
    gate_data = {
        "stage": stage,
        "agent": agent_type,
        "completed_at": datetime.utcnow().isoformat() + "Z",
        "summary": f"Agent '{agent_type}' has completed its work.",
        "outputs": outputs,
        "confluence_pages": [],
        "next_agent": NEXT_AGENT.get(stage, "unknown"),
        "review_questions": [],
        "concerns_flagged": [],
        "approval_command": f"/approve {stage}",
        "reject_command": f'/reject {stage} "your feedback"'
    }

    with open(gate_file, "w") as f:
        json.dump(gate_data, f, indent=2)

    # Write confluence-update-pending flag (Option B)
    flag_file = os.path.join(cwd, ".stagix", "state", "confluence-update-pending.json")
    with open(flag_file, "w") as f:
        json.dump({
            "agent": agent_type,
            "stage": stage,
            "completed_at": gate_data["completed_at"],
            "action": "update_last_modified_timestamp"
        }, f, indent=2)

    # Send desktop notification
    send_notification(
        f"Stagix: {agent_type} finished",
        f"Review needed. Run: /review-handoff {stage}"
    )

    # Print gate summary to terminal (stdout — visible to user)
    print(f"\n{'='*60}")
    print(f"  GATE: {stage}")
    print(f"  Agent: {agent_type}")
    print(f"  Status: Pending human review")
    print(f"{'='*60}")
    print(f"\n  Review: /review-handoff {stage}")
    print(f"  Approve: /approve {stage}")
    print(f"  Reject:  /reject {stage} \"your feedback\"")
    print(f"{'='*60}\n")

    sys.exit(0)


if __name__ == "__main__":
    main()
