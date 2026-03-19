#!/usr/bin/env python3
"""PreToolUse hook: Blocks dangerous bash commands.

Matcher: Bash(*)
Exit 0 = allow, Exit 2 = block
"""

import json
import sys
import os
import re
from datetime import datetime

BLOCKLIST = [
    (r"rm\s+-rf\s+/", "rm -rf / — filesystem destruction"),
    (r"rm\s+-rf\s+\*", "rm -rf * — recursive deletion"),
    (r"rm\s+-rf\s+\.\s", "rm -rf . — current directory destruction"),
    (r"DROP\s+TABLE", "DROP TABLE — database table destruction"),
    (r"DROP\s+DATABASE", "DROP DATABASE — database destruction"),
    (r"DELETE\s+FROM\s+\w+\s*;", "DELETE FROM without WHERE — mass data deletion"),
    (r"TRUNCATE\s+", "TRUNCATE — table data destruction"),
    (r"docker\s+system\s+prune", "docker system prune — removes all unused data"),
    (r"kubectl\s+delete\s+namespace", "kubectl delete namespace — namespace destruction"),
    (r"git\s+push\s+--force\s+(origin\s+)?(main|master)", "force push to main/master"),
    (r"git\s+push\s+-f\s+(origin\s+)?(main|master)", "force push to main/master"),
    (r"mkfs\.", "mkfs — filesystem formatting"),
    (r"dd\s+if=.+of=/dev/", "dd to device — disk overwrite"),
]


def main():
    data = json.load(sys.stdin)
    command = data.get("tool_input", {}).get("command", "")
    cwd = data.get("cwd", os.getcwd())

    for pattern, description in BLOCKLIST:
        if re.search(pattern, command, re.IGNORECASE):
            # Log the blocked attempt
            log_file = os.path.join(cwd, ".stagix", "security-events.log")
            try:
                os.makedirs(os.path.dirname(log_file), exist_ok=True)
                with open(log_file, "a") as f:
                    f.write(json.dumps({
                        "event": "destructive_command_blocked",
                        "command": command,
                        "pattern": description,
                        "timestamp": datetime.utcnow().isoformat() + "Z",
                        "agent": data.get("agent_type", "unknown")
                    }) + "\n")
            except OSError:
                pass

            print(f"Blocked: {description}", file=sys.stderr)
            print(f"Command: {command}", file=sys.stderr)
            print("Destructive commands are not allowed by Stagix safety hooks.", file=sys.stderr)
            sys.exit(2)

    sys.exit(0)


if __name__ == "__main__":
    main()
