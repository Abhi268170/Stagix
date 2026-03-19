# SPRINT-001: Phase 1 — Foundation

**Status**: DONE
**Priority**: P0 — Blocks everything
**Estimate**: ~8 files
**Dependencies**: None (first phase)

---

## Objective

Build the skeleton that every agent, hook, skill, and command plugs into. After this phase, MCP servers start, the project has a constitution, and the runtime config is in place.

---

## Tickets

### STGX-001: CLAUDE.md — Project Constitution Template
**Status**: TODO
**File**: `.stagix/CLAUDE.md`
**Description**: Parametrised project constitution that gets copied to the target project root. Auto-loaded by every Claude Code session. Contains:
- `{PROJECT_NAME}`, `{JIRA_KEY}`, `{CONFLUENCE_SPACE}` placeholders
- Agent role summary table (all 14 agents with file paths)
- devLoadAlwaysFiles list pointing to architecture shards
- MCP tool name registry (so agents reference correct names)
- Gate file locations
- Design principles summary
- File conventions

**Acceptance Criteria**:
- [ ] All 14 agents listed with correct file paths
- [ ] Placeholders are clearly marked for install.sh substitution
- [ ] devLoadAlwaysFiles section references coding-standards.md, tech-stack.md, source-tree.md
- [ ] MCP tool names match settings.json registration names

**BMAD Reuse**: None — built new per blueprint Section 3.2

---

### STGX-002: settings.json — MCP + Hooks Configuration
**Status**: TODO
**File**: `.stagix/settings.json`
**Description**: Claude Code project config. Registers all MCP servers and all hook event bindings. This is the operational backbone.

**MCP Servers to Register**:
```json
{
  "mcpServers": {
    "atlassian": {
      "command": "uvx",
      "args": ["mcp-atlassian"],
      "env": {
        "JIRA_URL": "${JIRA_URL}",
        "JIRA_EMAIL": "${JIRA_EMAIL}",
        "JIRA_API_TOKEN": "${JIRA_API_TOKEN}",
        "CONFLUENCE_URL": "${CONFLUENCE_URL}",
        "CONFLUENCE_EMAIL": "${CONFLUENCE_EMAIL}",
        "CONFLUENCE_API_TOKEN": "${CONFLUENCE_API_TOKEN}"
      }
    },
    "playwright": {
      "command": "npx",
      "args": [
        "@playwright/mcp@latest",
        "--headless",
        "--save-trace",
        "--save-video=1280x720",
        "--output-dir", ".stagix/qa/evidence/",
        "--test-id-attribute", "data-testid"
      ]
    }
  }
}
```

**Hook Event Bindings** (5 events, 9 scripts):
```json
{
  "hooks": {
    "PreToolUse": [
      { "matcher": "Bash(git commit*)", "hooks": [".stagix/hooks/pre-tool-use/block-git-commit.py"] },
      { "matcher": "Bash(*)", "hooks": [".stagix/hooks/pre-tool-use/block-destructive-ops.py"] },
      { "matcher": "Write|Edit", "hooks": [".stagix/hooks/pre-tool-use/validate-file-scope.py"] }
    ],
    "PostToolUse": [
      { "matcher": "Write|Edit", "hooks": [".stagix/hooks/post-tool-use/run-linter.py"] },
      { "matcher": "Write|Edit", "hooks": [".stagix/hooks/post-tool-use/log-file-changes.py"] }
    ],
    "Stop": [
      { "hooks": [".stagix/hooks/stop/handoff-gate.py"] }
    ],
    "TaskCompleted": [
      { "hooks": [".stagix/hooks/task-completed/enforce-dod.py"] }
    ],
    "SubagentStop": [
      { "hooks": [".stagix/hooks/subagent-stop/collect-output.py"] }
    ]
  }
}
```

**Acceptance Criteria**:
- [ ] Both MCP servers registered with correct commands and args
- [ ] Atlassian env vars use ${} placeholder syntax for install.sh substitution
- [ ] All 5 hook events bound with correct matchers
- [ ] Hook script paths are relative to .stagix/
- [ ] settings.json is valid JSON

**BMAD Reuse**: None — BMAD has no settings.json

---

### STGX-003: core-config.yaml — Runtime Configuration
**Status**: TODO
**File**: `.stagix/core-config.yaml`
**Description**: Runtime configuration read by agents, skills, and hooks. Parametrised with sensible defaults.

**Required Keys**:
```yaml
project:
  name: "{PROJECT_NAME}"
  jira_key: "{JIRA_KEY}"
  confluence_space: "{CONFLUENCE_SPACE}"
  mode: null  # Set by detect-stack: greenfield | brownfield

detected_stack:
  frontend: null
  backend: null
  database: null
  testing: null
  infrastructure: null
  package_managers: []

dev_server:
  command: null  # e.g., "uvicorn main:app --reload --port 8000"
  port: null
  health_check: null  # e.g., "http://localhost:8000/health"
  startup_dependencies: []  # Commands to run before dev server

quality:
  coverage_threshold: 80
  linters:
    ts: "eslint"
    tsx: "eslint"
    js: "eslint"
    py: "ruff"
    rb: "rubocop"
    go: "golangci-lint"

gates:
  location: ".stagix/gates/"
  planning_gates:
    - business-analyst
    - product-manager
    - ux-designer
    - solution-architect
    - db-designer
    - technical-writer
    - scrum-master
  engineering_gates:
    - devops
    - test-plan
    - security
    - tech-lead
    - qa
    - final

devLoadAlwaysFiles:
  - docs/architecture/coding-standards.md
  - docs/architecture/tech-stack.md
  - docs/architecture/source-tree.md
```

**Acceptance Criteria**:
- [ ] All keys from blueprint Section 3.2 present
- [ ] Sensible defaults for coverage_threshold (80%), linters
- [ ] Placeholders clearly marked for install.sh
- [ ] detected_stack section has nested keys for frontend, backend, database, testing, infrastructure
- [ ] YAML is valid and well-commented

**BMAD Reuse**: Adapt structure from BMAD core-config.yaml. Add detected_stack, quality, gates, dev_server sections (all new).

---

### STGX-004: install.sh — One-Command Installer
**Status**: TODO
**File**: `.stagix/install.sh`
**Description**: Shell script that copies .stagix/ into any target project and configures it.

**Steps**:
1. Check prerequisites (Node.js ≥ 18, Python ≥ 3.8, git)
2. Copy .stagix/ directory to target project root
3. Prompt for PROJECT_NAME, JIRA_KEY, CONFLUENCE_SPACE
4. Prompt for JIRA_URL, JIRA_EMAIL, JIRA_API_TOKEN
5. Prompt for CONFLUENCE_URL, CONFLUENCE_EMAIL, CONFLUENCE_API_TOKEN
6. Substitute all placeholders in CLAUDE.md and core-config.yaml
7. Write credentials to .env file (add to .gitignore)
8. Run detect-stack task (read signal files, write to core-config.yaml)
9. Install MCP dependencies: `npm install -g @playwright/mcp` (if not present)
10. Verify MCP servers can start
11. Create .stagix/gates/ directory with .gitkeep
12. Create .stagix/state/ directory with empty pipeline-log.json
13. Print success message with next steps

**Acceptance Criteria**:
- [ ] Works on Linux and macOS
- [ ] Prompts for all required values
- [ ] .env file created and .gitignore updated
- [ ] detect-stack runs and writes to core-config.yaml
- [ ] All placeholder substitution works
- [ ] Idempotent — safe to run multiple times

**BMAD Reuse**: Concept from BMAD's `npx bmad-method install`. Implementation is new.

---

### STGX-005: Mode Definitions
**Status**: TODO
**Files**:
- `.stagix/modes/greenfield.yaml`
- `.stagix/modes/brownfield.yaml`

**Description**: Define the agent activation sequence for each project mode. Read by orchestrators to determine workflow.

**greenfield.yaml**:
```yaml
name: Greenfield
description: New project — detect → plan → build
sequence:
  planning:
    - agent: business-analyst
      mode: sequential
      gate: business-analyst
    - agent: product-manager
      mode: sequential
      gate: product-manager
    - agent: ux-designer
      mode: parallel  # runs simultaneously with solution-architect
      gate: ux-designer
    - agent: solution-architect
      mode: parallel  # runs simultaneously with ux-designer
      gate: null  # gate after reviewing UX spec
    - agent: solution-architect
      mode: sequential  # reviews UX spec, finalises
      gate: solution-architect
    - agent: db-designer
      mode: sequential
      gate: db-designer
    - agent: technical-writer
      mode: sequential
      gate: technical-writer
    - agent: scrum-master
      mode: sequential
      gate: scrum-master  # Final Group 1 gate
  engineering:
    # Per-story sequence
    - agent: backend-dev
      mode: parallel  # with frontend-dev if independent
    - agent: frontend-dev
      mode: parallel
    - agent: devops
      mode: sequential
      gate: devops
    - agent: test-case-specialist
      mode: sequential
      gate: test-plan
    - agent: security-specialist
      mode: sequential
      gate: security
    - agent: tech-lead-reviewer
      mode: sequential
      gate: tech-lead
    - agent: qa-engineer
      mode: sequential
      gate: qa
```

**brownfield.yaml**: Same as greenfield but inserts `codebase-archaeologist` before `business-analyst` and uses brownfield story template.

**Acceptance Criteria**:
- [ ] Greenfield sequence matches blueprint Section 4.9
- [ ] Brownfield sequence matches blueprint Section 7
- [ ] UX Designer + Solution Architect marked as parallel
- [ ] Security → Tech Lead → QA marked as strictly sequential
- [ ] Valid YAML

**BMAD Reuse**: Structure from BMAD workflows/greenfield-fullstack.yaml (~60%). Add gate references and parallel markers.

---

### STGX-006: Gate Directory Setup
**Status**: TODO
**Files**:
- `.stagix/gates/.gitkeep`
- `.stagix/gates/README.md`

**Description**: Create the gates directory with documentation explaining the gate file format.

**README.md Contents**:
- Gate file types: `.pending.json`, `.approved`, `.rejected`
- JSON schema for .pending.json (stage, agent, completed_at, summary, outputs, confluence_pages, next_agent, review_questions, concerns_flagged, approval_command, reject_command)
- How /approve writes .approved file
- How /reject writes .rejected file with feedback
- How orchestrator reads gate state on next agent activation

**Acceptance Criteria**:
- [ ] Directory exists with .gitkeep
- [ ] README.md documents all three file types
- [ ] JSON schema matches blueprint Section 8.1
- [ ] Approval/rejection flow documented

**BMAD Reuse**: None — BMAD has no gate system

---

### STGX-007: State Directory Setup
**Status**: TODO
**Files**:
- `.stagix/state/active-agent.json`
- `.stagix/state/pipeline-log.json`

**Description**: Runtime state files. active-agent.json tracks which agent is currently running (read by validate-file-scope.py hook). pipeline-log.json tracks full pipeline history (read by /status command).

**active-agent.json schema**:
```json
{
  "agent": null,
  "group": null,
  "started_at": null,
  "story_key": null
}
```

**pipeline-log.json schema**:
```json
{
  "project": null,
  "mode": null,
  "events": []
}
```

**Acceptance Criteria**:
- [ ] Both files created with empty/null initial state
- [ ] Schemas documented in comments or companion README
- [ ] Valid JSON

**BMAD Reuse**: None

---

### STGX-008: Directory Scaffold
**Status**: TODO
**Description**: Create the full directory structure that all subsequent phases will populate.

**Directories to create**:
```
.stagix/
├── agents/planning/
├── agents/engineering/
├── tasks/planning/
├── tasks/engineering/
├── tasks/brownfield/
├── templates/
├── checklists/
├── skills/
├── hooks/pre-tool-use/
├── hooks/post-tool-use/
├── hooks/stop/
├── hooks/task-completed/
├── hooks/subagent-stop/
├── commands/
├── workflows/
├── modes/
├── gates/
├── state/
├── baselines/
├── tests/
├── qa/evidence/
├── qa/reports/
├── docs/
├── docs/architecture/
├── design-system/
├── design-system/pages/
```

**Acceptance Criteria**:
- [ ] All directories from blueprint Section 12 exist
- [ ] Each directory has .gitkeep where needed
- [ ] No extraneous directories

**BMAD Reuse**: None

---

## Smoke Test (Phase 1 Complete)

1. Run install.sh in a blank directory
2. Verify settings.json is valid JSON
3. Verify core-config.yaml is valid YAML
4. Verify all directories exist
5. Verify MCP servers can start (uvx mcp-atlassian --help, npx @playwright/mcp@latest --help)
6. Verify CLAUDE.md placeholders are substituted

## Definition of Done

- [ ] All 8 tickets completed
- [ ] Smoke test passes
- [ ] No broken references in CLAUDE.md
- [ ] settings.json loads without errors in Claude Code
