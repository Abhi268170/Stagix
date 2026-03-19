#!/usr/bin/env python3
"""PreToolUse hook: Enforces agent file scope boundaries.

Matcher: Write|Edit
Exit 0 = allow, Exit 2 = block

Reads active-agent.json to determine current agent, then checks if the
target file path is within the agent's permitted scope.
"""

import json
import sys
import os
import re

# Agent file scope definitions: agent_name → list of allowed path patterns (regex)
AGENT_SCOPES = {
    "business-analyst": [r"\.stagix/docs/project-brief\.md"],
    "product-manager": [r"\.stagix/docs/prd\.md"],
    "ux-designer": [r"\.stagix/docs/ux-spec\.md", r"\.stagix/design-system/"],
    "solution-architect": [r"\.stagix/docs/architecture", r"\.stagix/skills/.*/stacks/"],
    "db-designer": [r"\.stagix/docs/db-schema\.md"],
    "technical-writer": [],  # No local file writes — Confluence only
    "scrum-master": [],  # No local file writes — Jira only
    "codebase-archaeologist": [r"\.stagix/docs/brownfield-discovery\.md"],
    "backend-dev": [r"^(?!\.stagix/)(?!\.claude/)"],  # Anything outside .stagix/ and .claude/
    "frontend-dev": [r"^(?!\.stagix/)(?!\.claude/)"],
    "devops": [r"\.github/workflows/", r"docker-compose", r"Dockerfile", r"terraform/", r"Makefile", r"k8s/", r"\.gitlab-ci\.yml", r"\.circleci/"],
    "test-case-specialist": [r"\.stagix/tests/"],
    "security-specialist": [],  # Read-only — no writes allowed
    "tech-lead-reviewer": [],  # Read-only — no writes allowed
    "qa-engineer": [],  # No application file writes — Playwright + Confluence only
}


def main():
    data = json.load(sys.stdin)
    cwd = data.get("cwd", os.getcwd())
    tool_input = data.get("tool_input", {})

    # Extract target file path
    file_path = tool_input.get("file_path", tool_input.get("path", ""))
    if not file_path:
        sys.exit(0)  # No file path — allow (probably not a file write)

    # Make path relative to cwd
    if os.path.isabs(file_path):
        try:
            file_path = os.path.relpath(file_path, cwd)
        except ValueError:
            file_path = file_path  # Different drive on Windows

    # Read active agent
    active_agent_file = os.path.join(cwd, ".stagix", "state", "active-agent.json")
    if not os.path.exists(active_agent_file):
        sys.exit(0)  # No active agent tracking — allow (manual mode)

    with open(active_agent_file) as f:
        agent_state = json.load(f)

    agent_name = agent_state.get("agent")
    if not agent_name:
        # Also check agent_type from hook input (subagent context)
        agent_name = data.get("agent_type")

    if not agent_name:
        sys.exit(0)  # No agent identified — allow

    # Check if agent has scope restrictions
    if agent_name not in AGENT_SCOPES:
        sys.exit(0)  # Unknown agent — allow (probably manual usage)

    allowed_patterns = AGENT_SCOPES[agent_name]

    # Empty scope = no writes allowed at all
    if not allowed_patterns:
        deny(f"Agent '{agent_name}' is not permitted to write files. "
             f"Target: {file_path}. This agent is read-only or uses MCP tools exclusively.")

    # Check if file matches any allowed pattern
    for pattern in allowed_patterns:
        if re.search(pattern, file_path):
            sys.exit(0)  # Match found — allow

    deny(f"Agent '{agent_name}' is not permitted to write to '{file_path}'. "
         f"Allowed paths: {', '.join(allowed_patterns)}")


def deny(reason):
    """Output structured JSON denial per Claude Code PreToolUse spec."""
    output = {
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": reason
        }
    }
    print(json.dumps(output))
    sys.exit(0)  # Exit 0 with JSON — Claude Code reads the permissionDecision


if __name__ == "__main__":
    main()
