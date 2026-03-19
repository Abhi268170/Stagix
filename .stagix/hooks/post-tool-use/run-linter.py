#!/usr/bin/env python3
"""PostToolUse hook: Runs stack-appropriate linter after file writes.

Matcher: Write|Edit
Non-blocking — always exits 0. Lint output goes to stdout for agent context.
"""

import json
import sys
import os
import subprocess

# File extension → linter command mapping
# These can be overridden by core-config.yaml quality.linters section
DEFAULT_LINTERS = {
    ".ts": "npx eslint --no-error-on-unmatched-pattern",
    ".tsx": "npx eslint --no-error-on-unmatched-pattern",
    ".js": "npx eslint --no-error-on-unmatched-pattern",
    ".jsx": "npx eslint --no-error-on-unmatched-pattern",
    ".py": "ruff check",
    ".rb": "rubocop --format simple",
    ".go": "golangci-lint run",
    ".rs": "cargo clippy --message-format short",
}


def main():
    data = json.load(sys.stdin)
    cwd = data.get("cwd", os.getcwd())
    tool_input = data.get("tool_input", {})

    file_path = tool_input.get("file_path", tool_input.get("path", ""))
    if not file_path:
        sys.exit(0)

    # Determine file extension
    _, ext = os.path.splitext(file_path)
    if not ext or ext not in DEFAULT_LINTERS:
        sys.exit(0)  # No linter for this file type

    linter_cmd = DEFAULT_LINTERS[ext]

    # Make file path relative if absolute
    if os.path.isabs(file_path):
        try:
            file_path = os.path.relpath(file_path, cwd)
        except ValueError:
            pass

    full_cmd = f"{linter_cmd} {file_path}"

    try:
        result = subprocess.run(
            full_cmd,
            shell=True,
            cwd=cwd,
            capture_output=True,
            text=True,
            timeout=30
        )
        if result.returncode != 0 and result.stdout:
            # Output lint errors — agent will see these in context
            print(f"Lint issues in {file_path}:")
            print(result.stdout[:2000])  # Limit output
    except (subprocess.TimeoutExpired, FileNotFoundError):
        pass  # Linter not available — skip silently

    sys.exit(0)  # Never block — just inform


if __name__ == "__main__":
    main()
