#!/usr/bin/env python3
"""SubagentStop hook: Aggregates subagent output into pipeline log.

Fires when any spawned subagent completes and returns to the orchestrator.
Non-blocking — always exits 0.
"""

import json
import sys
import os
from datetime import datetime


def main():
    data = json.load(sys.stdin)
    cwd = data.get("cwd", os.getcwd())
    agent_type = data.get("agent_type", "unknown")

    # Prevent re-processing if already in a stop-hook continuation
    if data.get("stop_hook_active", False):
        sys.exit(0)

    # Append to pipeline log
    log_file = os.path.join(cwd, ".stagix", "state", "pipeline-log.json")
    try:
        if os.path.exists(log_file):
            with open(log_file) as f:
                log_data = json.load(f)
        else:
            log_data = {"project": None, "mode": None, "events": []}

        log_data["events"].append({
            "type": "agent_completed",
            "agent": agent_type,
            "timestamp": datetime.utcnow().isoformat() + "Z"
        })

        with open(log_file, "w") as f:
            json.dump(log_data, f, indent=2)
    except (json.JSONDecodeError, OSError):
        pass

    sys.exit(0)


if __name__ == "__main__":
    main()
