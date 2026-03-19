# {PROJECT_NAME} — Powered by Stagix

## Project Configuration

- **Jira Project Key**: {JIRA_KEY}
- **Confluence Space**: {CONFLUENCE_SPACE}
- **Runtime Config**: .stagix/core-config.yaml

## Agent Roles

This project uses Stagix, a 14-agent AI development orchestration system. Each agent has a bounded domain, a curated tool allowlist, and produces formal output that passes through a human approval gate.

### Planning Collective (Group 1)

| Agent | File | Domain |
|---|---|---|
| Planning Lead | .stagix/agents/planning/planning-lead.md | Orchestrates Group 1 specialists |
| Business Analyst (Priya) | .stagix/agents/planning/business-analyst.md | Requirements elicitation |
| Product Manager (Nate) | .stagix/agents/planning/product-manager.md | PRD creation |
| UX Designer (Lena) | .stagix/agents/planning/ux-designer.md | UX spec + design system |
| Solution Architect (Soren) | .stagix/agents/planning/solution-architect.md | System architecture |
| Database Designer (Rex) | .stagix/agents/planning/db-designer.md | Schema, indexes, migrations |
| Technical Writer (Alex) | .stagix/agents/planning/technical-writer.md | Confluence publishing |
| Scrum Master (Kai) | .stagix/agents/planning/scrum-master.md | Jira epic/story creation |
| Codebase Archaeologist (Sam) | .stagix/agents/planning/codebase-archaeologist.md | Brownfield discovery |

### Engineering Collective (Group 2)

| Agent | File | Domain |
|---|---|---|
| Engineering Lead | .stagix/agents/engineering/engineering-lead.md | Orchestrates Group 2 specialists |
| Backend Dev (Mira) | .stagix/agents/engineering/backend-dev.md | Backend implementation |
| Frontend Dev (Jamie) | .stagix/agents/engineering/frontend-dev.md | Frontend implementation |
| DevOps (Dev) | .stagix/agents/engineering/devops.md | CI/CD, Docker, IaC |
| Test Case Specialist (Tess) | .stagix/agents/engineering/test-case-specialist.md | Exhaustive test case writing |
| Security Specialist (Ash) | .stagix/agents/engineering/security-specialist.md | Read-only security audit |
| Tech Lead Reviewer (Morgan) | .stagix/agents/engineering/tech-lead-reviewer.md | 5-dimension code review |
| QA Engineer (River) | .stagix/agents/engineering/qa-engineer.md | Playwright browser-based QA |

## Developer Constraints

When implementing stories, the following files are always loaded as context. Treat them as immutable specifications, not suggestions.

devLoadAlwaysFiles:
- .stagix/docs/architecture/coding-standards.md
- .stagix/docs/architecture/tech-stack.md
- .stagix/docs/architecture/source-tree.md

## Gate System

Every agent boundary has a human approval gate. Gate files live in `.stagix/gates/`. No agent proceeds without an explicit `/approve {stage}` from the human.

- Pending: `.stagix/gates/{stage}.pending.json`
- Approved: `.stagix/gates/{stage}.approved`
- Rejected: `.stagix/gates/{stage}.rejected`

## Plugin Structure

Stagix is a Claude Code plugin. All agents, hooks, MCP servers, commands, and skills are declared in `.stagix/.claude-plugin/plugin.json`. Claude Code discovers everything automatically — no manual copying to `.stagix/agents/` needed.

## MCP Servers

MCP servers are registered in `.stagix/.claude-plugin/plugin.json` → `mcpServers`:

| Server | Command | Used By |
|---|---|---|
| Atlassian | `uvx mcp-atlassian` | Scrum Master, Technical Writer, Security, Tech Lead, QA, Engineering Lead |
| Playwright | `npx @playwright/mcp@latest` | QA Engineer, Test Case Specialist |

## Design Principles

1. One agent, one domain — enforced by tool allowlists in agent frontmatter
2. Human gates at every boundary — file-based, deterministic
3. Documents before code — architecture designed and approved before implementation
4. Stack agnosticism — detect-stack + SKILL.md loaders compose correct knowledge at runtime
5. Hooks for enforcement — PreToolUse blocks bad actions structurally
6. Jira and Confluence as permanent record — audit trail is a byproduct
7. Brownfield discovery before planning — Archaeologist maps legacy codebases first

## Slash Commands

| Command | What It Does |
|---|---|
| `/start-project "idea"` | Detects stack/mode, launches Planning Collective |
| `/implement-story PROJ-123` | Fetches story from Jira, launches Engineering Collective |
| `/approve {stage}` | Writes gate approval, unlocks next agent |
| `/reject {stage} "reason"` | Writes rejection, agent re-runs with feedback |
| `/review-handoff {stage}` | Shows pending gate file for review |
| `/status` | Pipeline state, pending gates, Jira sprint status |
| `/discover-brownfield` | Triggers Archaeologist in isolation |
