#!/usr/bin/env python3
"""PostToolUse hook: Logs every file change to pipeline-log.json.

Matcher: Write|Edit
Non-blocking — always exits 0. Silent operation.
"""

import json
import sys
import os
from datetime import datetime


def main():
    data = json.load(sys.stdin)
    cwd = data.get("cwd", os.getcwd())
    tool_input = data.get("tool_input", {})
    tool_name = data.get("tool_name", "unknown")

    file_path = tool_input.get("file_path", tool_input.get("path", ""))
    if not file_path:
        sys.exit(0)

    # Make relative
    if os.path.isabs(file_path):
        try:
            file_path = os.path.relpath(file_path, cwd)
        except ValueError:
            pass

    # Read current agent
    agent_name = data.get("agent_type", "unknown")
    active_agent_file = os.path.join(cwd, ".stagix", "state", "active-agent.json")
    if os.path.exists(active_agent_file):
        try:
            with open(active_agent_file) as f:
                agent_state = json.load(f)
                agent_name = agent_state.get("agent", agent_name)
        except (json.JSONDecodeError, OSError):
            pass

    # Append to pipeline log
    log_file = os.path.join(cwd, ".stagix", "state", "pipeline-log.json")
    try:
        if os.path.exists(log_file):
            with open(log_file) as f:
                log_data = json.load(f)
        else:
            log_data = {"project": None, "mode": None, "events": []}

        log_data["events"].append({
            "type": "file_change",
            "agent": agent_name,
            "file": file_path,
            "action": tool_name.lower(),
            "timestamp": datetime.utcnow().isoformat() + "Z"
        })

        with open(log_file, "w") as f:
            json.dump(log_data, f, indent=2)
    except (json.JSONDecodeError, OSError):
        pass  # Don't fail on logging errors

    sys.exit(0)


if __name__ == "__main__":
    main()
