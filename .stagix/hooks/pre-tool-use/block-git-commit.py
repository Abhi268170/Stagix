#!/usr/bin/env python3
"""PreToolUse hook: Blocks git commits unless all quality gates are passed.

Matcher: Bash(git commit*)
Exit 0 = allow commit, Exit 2 = block commit (stderr shown to Claude)
"""

import json
import sys
import os
import glob
import subprocess

def main():
    data = json.load(sys.stdin)
    cwd = data.get("cwd", os.getcwd())
    command = data.get("tool_input", {}).get("command", "")

    # Only act on git commit commands — skip everything else
    if not command.strip().startswith("git commit"):
        sys.exit(0)

    stagix_dir = os.path.join(cwd, ".stagix")

    # Read active agent context
    active_agent_file = os.path.join(stagix_dir, "state", "active-agent.json")
    story_key = None
    if os.path.exists(active_agent_file):
        with open(active_agent_file) as f:
            agent_state = json.load(f)
            story_key = agent_state.get("story_key")

    # Check 1: Tech Lead gate must be approved
    gates_dir = os.path.join(stagix_dir, "gates")
    tech_lead_approved = glob.glob(os.path.join(gates_dir, "tech-lead.approved"))
    if not tech_lead_approved:
        print("Cannot commit: Tech Lead review gate not passed.", file=sys.stderr)
        if story_key:
            print(f"Story: {story_key}", file=sys.stderr)
        print("Run the full engineering review pipeline before committing.", file=sys.stderr)
        sys.exit(2)

    # Check 2: Story DoD checklist
    dod_file = os.path.join(stagix_dir, "checklists", "story-dod-checklist.md")
    if os.path.exists(dod_file):
        with open(dod_file) as f:
            content = f.read()
        unchecked = content.count("- [ ]")
        if unchecked > 0:
            print(f"Cannot commit: {unchecked} Definition of Done items still unchecked.", file=sys.stderr)
            print("Complete the story-dod-checklist.md before committing.", file=sys.stderr)
            sys.exit(2)

    # Check 3: Run test suite
    config_file = os.path.join(stagix_dir, "core-config.yaml")
    test_command = None
    coverage_threshold = 80

    if os.path.exists(config_file):
        with open(config_file) as f:
            config_content = f.read()
        # Simple YAML parsing for test command detection
        # Look for detected testing framework to determine test command
        if "pytest" in config_content:
            test_command = "python -m pytest --tb=short -q"
        elif "jest" in config_content or "vitest" in config_content:
            test_command = "npx jest --ci" if "jest" in config_content else "npx vitest run"
        elif "go-testing" in config_content:
            test_command = "go test ./..."
        elif "rspec" in config_content:
            test_command = "bundle exec rspec"

        # Extract coverage threshold
        for line in config_content.split("\n"):
            if "coverage_threshold:" in line:
                try:
                    coverage_threshold = int(line.split(":")[1].strip())
                except (ValueError, IndexError):
                    pass

    if test_command:
        try:
            result = subprocess.run(
                test_command,
                shell=True,
                cwd=cwd,
                capture_output=True,
                text=True,
                timeout=300
            )
            if result.returncode != 0:
                print("Cannot commit: Test suite failed.", file=sys.stderr)
                print(f"Command: {test_command}", file=sys.stderr)
                if result.stderr:
                    # Show last 20 lines of test output
                    lines = result.stderr.strip().split("\n")[-20:]
                    print("\n".join(lines), file=sys.stderr)
                sys.exit(2)
        except subprocess.TimeoutExpired:
            print("Cannot commit: Test suite timed out (300s limit).", file=sys.stderr)
            sys.exit(2)
        except FileNotFoundError:
            # Test command not found — skip test check
            pass

    # All checks passed
    sys.exit(0)


if __name__ == "__main__":
    main()
