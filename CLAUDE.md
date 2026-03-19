# STAGIX — AI-Native Agile Development Orchestration System

## What This Project Is

Stagix is a portable `.stagix/` directory (~186 files) that transforms Claude Code CLI into a 14-agent software engineering team. Drop it into any project and get a fully-staffed AI development organisation with structured Agile methodology, human approval gates at every boundary, and full Jira/Confluence/Playwright integration.

**Canonical spec**: `docs/Stagix-Blueprint.pdf` (58 pages, v1.0)
**Inspiration source**: `reference/.bmad-core/` (75 files, BMAD Method v4.44.3)

## Core Architecture

### Two Groups, Sequential

- **Group 1 — Planning Collective** (8 agents): Think, define, document, plan. Output = Confluence docs + Jira stories.
- **Group 2 — Engineering Collective** (7 agents): Build, test, review, ship. Activated per-story after Group 1 approval.

Group 2 cannot start until Group 1's final gate (Scrum Master) is approved.

### The 14 Agents

**Planning (Group 1):**
| Agent | File | Role |
|---|---|---|
| Planning Lead | `.stagix/agents/planning/planning-lead.md` | Orchestrator — Agent Team LEAD mode |
| Business Analyst (Priya) | `.stagix/agents/planning/business-analyst.md` | Requirements elicitation (interactive) |
| Product Manager (Nate) | `.stagix/agents/planning/product-manager.md` | PRD creation |
| UX Designer (Lena) | `.stagix/agents/planning/ux-designer.md` | UX spec + design system |
| Solution Architect (Soren) | `.stagix/agents/planning/solution-architect.md` | System architecture + sharded files |
| Database Designer (Rex) | `.stagix/agents/planning/db-designer.md` | Schema, indexes, migrations |
| Technical Writer (Alex) | `.stagix/agents/planning/technical-writer.md` | Confluence publishing |
| Scrum Master (Kai) | `.stagix/agents/planning/scrum-master.md` | Jira epic/story creation |
| Codebase Archaeologist (Sam) | `.stagix/agents/planning/codebase-archaeologist.md` | Brownfield discovery (brownfield only) |

**Engineering (Group 2):**
| Agent | File | Role |
|---|---|---|
| Engineering Lead | `.stagix/agents/engineering/engineering-lead.md` | Orchestrator — spawns subagents |
| Backend Dev (Mira) | `.stagix/agents/engineering/backend-dev.md` | Backend implementation |
| Frontend Dev (Jamie) | `.stagix/agents/engineering/frontend-dev.md` | Frontend implementation |
| DevOps (Dev) | `.stagix/agents/engineering/devops.md` | CI/CD, Docker, IaC |
| Test Case Specialist (Tess) | `.stagix/agents/engineering/test-case-specialist.md` | Exhaustive test case writing |
| Security Specialist (Ash) | `.stagix/agents/engineering/security-specialist.md` | Read-only security audit |
| Tech Lead Reviewer (Morgan) | `.stagix/agents/engineering/tech-lead-reviewer.md` | 5-dimension code review |
| QA Engineer (River) | `.stagix/agents/engineering/qa-engineer.md` | Playwright browser-based QA |

### Key Primitives Used

- **CLAUDE.md**: Project constitution (this file) — auto-loaded by every session
- **settings.json**: MCP servers (Atlassian, Playwright) + 5 hook event bindings
- **core-config.yaml**: Runtime config (Jira key, Confluence space, detected stack, thresholds)
- **Agent files (.md)**: Persona + role + tool allowlist + skills + commands per agent
- **Skills (.stagix/skills/)**: Domain knowledge with base.md + stack overlays, loaded via SKILL.md
- **Hooks (.stagix/hooks/)**: Python enforcement scripts for 5 Claude Code hook events
- **Gate files (.stagix/gates/)**: JSON state machine for human approval workflow
- **Slash commands (.stagix/commands/)**: Human entry points as SKILL.md files

### MCP Servers (3)

1. **Atlassian** (`uvx mcp-atlassian`): Jira + Confluence — 72 tools
2. **Playwright** (`npx @playwright/mcp@latest`): Browser automation — headless, trace+screenshot saving
3. **Figma** (already configured): Design-to-code workflows

### External Skills

- **UI UX Pro Max** (`npm install -g uipro-cli && uipro init --ai claude`): 161 industry rules, 67 styles, design system generation

## Design Principles (Non-Negotiable)

1. **Specialisation over generalism** — one agent, one domain, enforced by tool allowlists
2. **Human gates at every boundary** — file-based, deterministic, not conversational
3. **Documents before code** — architecture/schema/UX designed and approved before any implementation
4. **Stack agnosticism by runtime composition** — detect-stack + SKILL.md loaders compose correct knowledge
5. **Hooks for enforcement, not reminders** — PreToolUse blocks bad actions, not prompts
6. **Jira and Confluence as permanent record** — audit trail is a byproduct, not extra work
7. **Brownfield discovery before brownfield planning** — Archaeologist runs first in legacy codebases
8. **Parallel where safe, sequential where critical** — UX+Architect parallel; Security→TechLead→QA sequential
9. **Self-populating knowledge base** — unknown stacks trigger Architect to generate new skill overlays

## Hard Constraints from Claude Code

- Subagents cannot spawn subagents (one-level deep only)
- Agent Teams have no per-agent hooks (Stagix uses subagents for specialists, teams only for Planning Lead)
- Hooks apply per-project, not per-agent (agent-specific enforcement via hook scripts reading active-agent.json)
- MCP tools must be pre-registered in settings.json
- Context windows are finite (mitigated by sharded docs + curated always-load files)

## Build Plan

10 phases, dependency-ordered. See `docs/implementation-plan.md` for full detail.
Total estimated files: ~186. Build reference: `docs/Stagix-Blueprint.pdf` pages 50-53.

## BMAD Reuse Strategy

BMAD (`reference/.bmad-core/`) provides reusable content for:
- Agent personas and principles (~60% reuse, adapt container format)
- Templates (~80% reuse, enhance with Stagix-specific fields)
- Checklists (~90% reuse, enforce via hooks instead of advisory)
- Data files (elicitation methods, test frameworks — reuse verbatim as skill base.md content)
- Workflow structures (~70% reuse, add gate refs + parallel markers)

What Stagix builds NEW beyond BMAD:
- Gate file system, hook enforcement scripts, MCP integration, skill domains with stack overlays, detect-stack, Archaeologist agent, Engineering Lead orchestrator, Security/TechLead/QA as separate agents, Playwright browser QA, slash commands, pipeline state tracking

## File Conventions

- Agent definitions: `.stagix/agents/{group}/{name}.md`
- Tasks: `.stagix/tasks/{phase}/{name}.md`
- Templates: `.stagix/templates/{name}.yaml`
- Skills: `.stagix/skills/{domain}/SKILL.md` + `base.md` + `stacks/{framework}.md`
- Hooks: `.stagix/hooks/{event-type}/{name}.py`
- Gates: `.stagix/gates/{stage}.pending.json` / `.approved` / `.rejected`
- Commands: `.stagix/commands/{name}/SKILL.md`
- State: `.stagix/state/active-agent.json`, `pipeline-log.json`
