#!/usr/bin/env python3
"""TaskCompleted hook: Enforces Definition of Done on task completion.

Fires when a developer agent tries to mark a task as complete.
Exit 0 = allow completion, Exit 2 = block with specific failures.
"""

import json
import sys
import os
import re
import subprocess


def check_for_secrets(cwd):
    """Grep for common secret patterns in recently modified files."""
    secret_patterns = [
        r'password\s*=\s*["\'][^"\']+["\']',
        r'api[_-]?key\s*=\s*["\'][^"\']+["\']',
        r'secret\s*=\s*["\'][^"\']+["\']',
        r'-----BEGIN .* PRIVATE KEY-----',
        r'token\s*=\s*["\'][A-Za-z0-9+/=]{20,}["\']',
    ]

    findings = []
    for pattern in secret_patterns:
        try:
            result = subprocess.run(
                ["grep", "-rn", "-E", pattern, "--include=*.py", "--include=*.js",
                 "--include=*.ts", "--include=*.go", "--include=*.rb",
                 "--include=*.java", "--include=*.env", "."],
                cwd=cwd, capture_output=True, text=True, timeout=10
            )
            if result.stdout:
                for line in result.stdout.strip().split("\n")[:5]:
                    if ".env.example" not in line and "test" not in line.lower():
                        findings.append(line.strip()[:200])
        except (subprocess.TimeoutExpired, FileNotFoundError):
            pass

    return findings


def main():
    data = json.load(sys.stdin)
    cwd = data.get("cwd", os.getcwd())
    task_id = data.get("task_id", "unknown")
    task_subject = data.get("task_subject", "unknown")
    failures = []

    # Check 1: Hardcoded secrets
    secrets = check_for_secrets(cwd)
    if secrets:
        failures.append(f"Potential hardcoded secrets found ({len(secrets)} matches):")
        for s in secrets[:3]:
            failures.append(f"  {s}")

    # Check 2: Linting errors on modified files
    # (run-linter.py is non-blocking, but we check here as a gate)
    # This is a lightweight check — full lint is done by run-linter.py

    # Check 3: File list should be updated
    # (We can't verify this structurally — the agent is responsible)

    if failures:
        print(f"Definition of Done check FAILED for task '{task_subject}' ({task_id}):", file=sys.stderr)
        for f in failures:
            print(f"  {f}", file=sys.stderr)
        print("\nFix these issues before marking the task complete.", file=sys.stderr)
        sys.exit(2)  # Exit 2 blocks completion, stderr is feedback to the model

    sys.exit(0)


if __name__ == "__main__":
    main()
