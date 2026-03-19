# SPRINT-005: Phase 5 — Hook System

**Status**: DONE
**Priority**: P0 — Enforcement layer, required before integration testing
**Estimate**: ~9 Python scripts + settings.json wiring
**Dependencies**: SPRINT-001 (Foundation — settings.json hook bindings)

---

## Objective

Build all 9 hook enforcement scripts. After this phase, quality is structurally enforced: git commits blocked without gate approval, file writes blocked outside agent scope, linters run automatically, gate files written on agent completion.

**Design Decision (Resolved)**: Hooks use Option B — they only read/write local files. No direct API calls to Atlassian or any external service. The `update-confluence-status.py` hook writes a flag file; the next agent reads it and updates Confluence via MCP on activation.

---

## Tickets

### STGX-043: block-git-commit.py (PreToolUse)
**Status**: TODO
**File**: `.stagix/hooks/pre-tool-use/block-git-commit.py`
**Matcher**: `Bash(git commit*)`
**Description**: The single most important hook. No code reaches git history without passing the full quality stack.

**Logic**:
1. Read .stagix/state/active-agent.json to get current story key
2. Read .stagix/gates/ for current story's tech-lead gate file
3. Verify tech-lead.approved exists — if not, block with: 'Cannot commit: Tech Lead review gate not passed for story {story-key}'
4. Run story-dod-checklist.md verification: all task checkboxes checked, File List is complete, Change Log updated
5. Run full test suite via stack-appropriate test command from core-config.yaml
6. Check test coverage meets threshold from core-config.yaml (default: 80%)
7. If ALL pass: allow commit (exit 0)
8. If ANY fail: block with specific error listing what failed (exit 2)

**Acceptance Criteria**:
- [ ] Blocks commit if tech-lead gate not approved
- [ ] Blocks commit if DoD checklist incomplete
- [ ] Blocks commit if tests fail
- [ ] Blocks commit if coverage below threshold
- [ ] Clear error messages for each failure type
- [ ] Exit code 2 to block, 0 to allow

---

### STGX-044: block-destructive-ops.py (PreToolUse)
**Status**: TODO
**File**: `.stagix/hooks/pre-tool-use/block-destructive-ops.py`
**Matcher**: `Bash(*)`
**Description**: Blocks dangerous bash commands.

**Blocklist**:
- `rm -rf /` and variants
- `DROP TABLE`, `DROP DATABASE`
- `DELETE FROM` without WHERE
- `TRUNCATE` on production tables
- `docker system prune`
- `kubectl delete namespace`
- `git push --force` to main/master

**Logic**: Pattern match command against blocklist. If match: block with explicit error, log to .stagix/security-events.log.

**Acceptance Criteria**:
- [ ] All patterns from blueprint Section 10.3 blocked
- [ ] Clear error message explaining why blocked
- [ ] Logged to security-events.log
- [ ] Does not false-positive on safe commands

---

### STGX-045: validate-file-scope.py (PreToolUse)
**Status**: TODO
**File**: `.stagix/hooks/pre-tool-use/validate-file-scope.py`
**Matcher**: `Write|Edit`
**Description**: Enforces agent file scope boundaries. The real security boundary of the system.

**Logic**:
1. Read .stagix/state/active-agent.json to get current agent
2. Read the agent's definition file to get permitted file scope
3. Extract the target file path from the tool call
4. Validate target path against agent's permitted scope
5. If outside scope: block with 'Agent {name} is not permitted to write to {path}'

**Examples**:
- Security Specialist attempting to write src/ → BLOCKED
- Scrum Master attempting to write anything except via Jira MCP → BLOCKED
- Developer attempting to edit ux-spec.md → BLOCKED
- Backend Dev writing to src/api/routes.py → ALLOWED

**Acceptance Criteria**:
- [ ] Reads active-agent.json correctly
- [ ] Parses agent definition for file scope
- [ ] Blocks out-of-scope writes
- [ ] Allows in-scope writes
- [ ] Clear error messages
- [ ] Handles case where no active agent is set (allow — manual mode)

---

### STGX-046: run-linter.py (PostToolUse)
**Status**: TODO
**File**: `.stagix/hooks/post-tool-use/run-linter.py`
**Matcher**: `Write|Edit`
**Description**: Runs stack-appropriate linter after every file write/edit. Non-blocking — appends lint errors to agent context.

**Logic**:
1. Detect file extension of changed file
2. Look up linter from core-config.yaml quality.linters section
3. Run linter on changed file only (not whole project)
4. If lint errors: append to agent context as informational message
5. Does NOT block — just informs

**Linter Mapping**:
- .ts/.tsx/.js/.jsx → eslint
- .py → ruff
- .rb → rubocop
- .go → golangci-lint
- Others → skip

**Acceptance Criteria**:
- [ ] Correct linter selected per file extension
- [ ] Runs on single file, not whole project
- [ ] Non-blocking (exit 0 always)
- [ ] Lint output appended to agent context
- [ ] Gracefully handles missing linter (skip with warning)

---

### STGX-047: log-file-changes.py (PostToolUse)
**Status**: TODO
**File**: `.stagix/hooks/post-tool-use/log-file-changes.py`
**Matcher**: `Write|Edit`
**Description**: Logs every file change to pipeline-log.json for auditing and /status command.

**Logic**: Append entry to .stagix/state/pipeline-log.json:
```json
{
  "type": "file_change",
  "agent": "{active_agent}",
  "file": "{changed_file_path}",
  "action": "write|edit",
  "timestamp": "{ISO-8601}"
}
```

**Acceptance Criteria**:
- [ ] Every Write/Edit logged
- [ ] Correct agent attribution from active-agent.json
- [ ] Valid JSON maintained in pipeline-log.json
- [ ] Silent — no output to agent

---

### STGX-048: handoff-gate.py (Stop)
**Status**: TODO
**File**: `.stagix/hooks/stop/handoff-gate.py`
**Description**: The orchestration backbone. Fires when any agent produces its final response. Writes structured gate file and notifies human.

**Logic**:
1. Read .stagix/state/active-agent.json to get completing agent
2. Read agent's output files from File List in story or docs/ directory
3. Write structured .stagix/gates/{stage}.pending.json:
   ```json
   {
     "stage": "{stage_name}",
     "agent": "{Agent Name}",
     "completed_at": "{ISO-8601}",
     "summary": "{extracted from agent output}",
     "outputs": ["{list of files produced}"],
     "confluence_pages": ["{URLs if any}"],
     "next_agent": "{next in sequence}",
     "review_questions": ["{specific questions for reviewer}"],
     "concerns_flagged": ["{any issues agent noted}"],
     "approval_command": "/approve {stage}",
     "reject_command": "/reject {stage} \"your feedback\""
   }
   ```
4. Send desktop notification: `notify-send` (Linux) or `osascript` (macOS)
5. Print formatted summary to terminal with /approve and /reject commands
6. Write confluence-update-pending flag file (for next agent to process — Option B)

**Acceptance Criteria**:
- [ ] Gate file written with all fields
- [ ] Desktop notification sent
- [ ] Terminal output clearly shows what to review and how to approve/reject
- [ ] Confluence update flag written for next agent
- [ ] Works for both planning and engineering agents

---

### STGX-049: enforce-dod.py (TaskCompleted)
**Status**: TODO
**File**: `.stagix/hooks/task-completed/enforce-dod.py`
**Description**: Fires when developer agent tries to mark a task as complete. Validates Definition of Done.

**Logic**:
1. Read story-dod-checklist.md
2. Validate:
   - All functional requirements for this task are implemented
   - Tests for this task written and passing
   - No linting errors on files modified in this task
   - File List updated with any new/modified files
   - No hardcoded secrets or credentials in modified files
3. If ALL pass: allow task completion
4. If ANY fail: block completion, output exactly which items failed and why

**Acceptance Criteria**:
- [ ] All DoD items checked
- [ ] Blocks completion on failure with specific items listed
- [ ] Checks for hardcoded secrets (pattern match for API keys, passwords, tokens)
- [ ] Validates File List is current

---

### STGX-050: collect-output.py (SubagentStop)
**Status**: TODO
**File**: `.stagix/hooks/subagent-stop/collect-output.py`
**Description**: Fires when any spawned subagent completes. Aggregates output into parent orchestrator's context.

**Logic**:
1. Read subagent's output from task completion message
2. Append structured summary to .stagix/state/pipeline-log.json:
   ```json
   {
     "type": "agent_completed",
     "agent": "{agent_name}",
     "story_key": "{if applicable}",
     "outputs": ["{files produced}"],
     "status": "success|failure",
     "summary": "{brief output summary}",
     "timestamp": "{ISO-8601}"
   }
   ```
3. Update orchestrator's awareness of pipeline progress

**Acceptance Criteria**:
- [ ] Subagent output captured
- [ ] Pipeline log updated
- [ ] Orchestrator can reconstruct state from pipeline-log.json

---

### STGX-051: Wire Hooks in settings.json
**Status**: TODO
**Description**: Verify all hook bindings in settings.json match the actual script paths and matchers. This is a validation ticket — the bindings were defined in STGX-002 but this verifies they work with the actual scripts.

**Acceptance Criteria**:
- [ ] All 9 scripts exist at paths referenced in settings.json
- [ ] Matchers fire on correct events
- [ ] Scripts are executable (chmod +x)
- [ ] Python shebang line present (#!/usr/bin/env python3)

---

## Smoke Test (Phase 5 Complete)

1. Trigger a git commit without gate approval → verify blocked
2. Attempt `rm -rf /` via Bash → verify blocked
3. As Security Specialist, attempt to Write to src/ → verify blocked
4. Write a .py file → verify ruff runs automatically
5. Complete an agent → verify gate file written + notification sent

## Definition of Done

- [ ] All 9 tickets completed (STGX-043 through STGX-051)
- [ ] All hooks fire on correct events
- [ ] block-git-commit.py blocks commits without gate approval
- [ ] validate-file-scope.py enforces agent boundaries
- [ ] handoff-gate.py writes gate files and notifies human
