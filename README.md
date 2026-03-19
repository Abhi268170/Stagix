<p align="center">
  <img src="stagix-overview.png" alt="Stagix — AI-Native Agile Development Orchestration for Claude Code" width="100%">
</p>

<p align="center">
  <strong>Drop a 14-agent engineering team into any project via Claude Code.</strong><br>
  Structured Agile workflow. Human gates at every boundary. Full Jira, Confluence & Playwright integration.
</p>

<p align="center">
  <a href="#quick-start">Quick Start</a> &bull;
  <a href="#the-14-agents">Agents</a> &bull;
  <a href="#how-it-works">How It Works</a> &bull;
  <a href="#slash-commands">Commands</a> &bull;
  <a href="#stack-agnosticism">Stack Support</a> &bull;
  <a href="#enforcement-hooks">Hooks</a>
</p>

---

```bash
npx stagix install .
claude --plugin-dir .stagix
/start-project "your idea"
```

## What It Does

Stagix is a [Claude Code](https://code.claude.com) plugin that transforms the CLI into a fully-staffed AI development organisation. Instead of one agent doing everything in a single context window, Stagix splits the work across 14 specialist agents — each with a bounded domain, curated tools, and a human approval gate.

**The problem it solves:** Current AI coding tools treat the entire development lifecycle as one monolithic session. Requirements drift into assumptions, architecture is never documented, tests are afterthoughts, security is ignored until incident time, and there's no audit trail.

**How Stagix fixes it:** Two sequential collectives. The Planning Collective (8 agents) elicits requirements, designs architecture, creates schemas, publishes to Confluence, and creates Jira stories. The Engineering Collective (7 agents) implements, tests, reviews security, performs code review across 5 dimensions, and runs browser-based QA via Playwright. Every handoff has a human gate. Every decision is traceable.

## Quick Start

### Prerequisites

- [Claude Code](https://code.claude.com) CLI installed
- Node.js >= 18
- Python >= 3.8
- Git
- Atlassian account (Jira + Confluence) with [API token](https://id.atlassian.com/manage-profile/security/api-tokens)

### Install

```bash
npx stagix install .
```

This copies `.stagix/` into your project and creates a `.env` template for credentials.

### Configure Credentials

Edit `.stagix/.env` with your Atlassian details:

```env
JIRA_URL=https://yourorg.atlassian.net
JIRA_EMAIL=your-email@example.com
JIRA_API_TOKEN=your-api-token
CONFLUENCE_URL=https://yourorg.atlassian.net
CONFLUENCE_EMAIL=your-email@example.com
CONFLUENCE_API_TOKEN=your-api-token
```

### Launch

```bash
claude --plugin-dir .stagix
```

### Start Building

```bash
# New project
/start-project "A SaaS project management tool for small teams"

# Existing codebase
/discover-brownfield
```

## The 14 Agents

### Planning Collective (Group 1)

| Agent | Name | What It Does |
|---|---|---|
| Planning Lead | — | Orchestrates Group 1, manages gates and sequencing |
| Business Analyst | Priya | Multi-turn requirements elicitation with structured 5-phase protocol |
| Product Manager | Nate | PRD with epics, personas, prioritisation, NFRs |
| UX Designer | Lena | UX spec + design system via [UI UX Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) |
| Solution Architect | Soren | System architecture, coding standards, API contracts, sharded docs |
| Database Designer | Rex | Schema, indexes, migration strategy, query patterns |
| Technical Writer | Alex | Publishes all docs to Confluence with cross-links and labels |
| Scrum Master | Kai | Creates Jira epics and fully-detailed stories from design docs |
| Codebase Archaeologist | Sam | Brownfield-only: reads and maps existing codebases before planning |

### Engineering Collective (Group 2)

| Agent | Name | What It Does |
|---|---|---|
| Engineering Lead | — | Orchestrates Group 2, validates stories, manages failure routing |
| Backend Dev | Mira | Implements backend tasks, writes tests, follows architecture constraints |
| Frontend Dev | Jamie | Implements UI with design system compliance, accessibility checks |
| DevOps | Dev | CI/CD, Docker, IaC updates, regression baselines |
| Test Case Specialist | Tess | Writes exhaustive test cases BEFORE developers implement them |
| Security Specialist | Ash | Read-only OWASP audit, CRITICAL/HIGH findings block the story |
| Tech Lead Reviewer | Morgan | 5-dimension code review: quality, security, tests, architecture, performance |
| QA Engineer | River | Browser-based acceptance testing via Playwright MCP |

## How It Works

```
/start-project "idea"
    │
    ▼
┌─────────────────────────────────────────────┐
│  GROUP 1 — PLANNING COLLECTIVE              │
│                                             │
│  BA → PM → UX + Architect → DB → Writer → SM│
│  ↕      ↕       ↕           ↕    ↕       ↕ │
│  gate   gate    gate        gate gate   gate│
└─────────────────────────────────────────────┘
    │ /approve scrum-master (unlocks Group 2)
    ▼
┌─────────────────────────────────────────────┐
│  GROUP 2 — ENGINEERING COLLECTIVE (per story)│
│                                             │
│  Backend + Frontend → DevOps → Test Cases   │
│  → Test Implementation → Security → Tech    │
│  Lead → QA → Final Human Approval           │
└─────────────────────────────────────────────┘
    │ /approve final PROJ-123
    ▼
  Story → Done in Jira
```

Every arrow is a human gate. You review output, then run `/approve {stage}` or `/reject {stage} "feedback"`. Nothing proceeds without your explicit approval.

## Slash Commands

| Command | What It Does |
|---|---|
| `/start-project "idea"` | Detects stack, launches Planning Collective |
| `/implement-story PROJ-123` | Fetches story from Jira, launches Engineering Collective |
| `/approve {stage}` | Approves a gate, unlocks next agent |
| `/reject {stage} "reason"` | Rejects with feedback, agent re-runs |
| `/review-handoff {stage}` | Shows what an agent produced for review |
| `/status` | Pipeline state, pending gates, Jira sprint status |
| `/discover-brownfield` | Triggers codebase analysis on existing projects |

## Stack Agnosticism

Stagix detects your tech stack automatically and loads the correct domain knowledge at runtime. No hardcoded assumptions.

**12 skill domains** with **69 stack overlays** covering:

| Domain | Overlays |
|---|---|
| Backend | FastAPI, Django, Express, NestJS, Rails, Gin, Spring, ASP.NET, Laravel, Actix |
| Frontend | Next.js, Vite+React, Vue+Nuxt, SvelteKit, Angular, Astro, Tailwind |
| Testing | Jest, Vitest, Pytest, RSpec, Go testing, JUnit, xUnit, Playwright |
| Database | PostgreSQL, MySQL, MongoDB, SQLite, Redis, DynamoDB, CockroachDB |
| Security | Python, Node, Rails, Java, PHP, Go |
| API Design | REST/OpenAPI, GraphQL, gRPC, WebSocket |
| Infrastructure | Docker Compose, Kubernetes, Terraform (AWS/GCP), GitHub Actions, GitLab CI, CircleCI |
| Migrations | Alembic, Flyway, Liquibase, ActiveRecord, Prisma, TypeORM, GORM, Goose |

Unknown stacks get a `_generic` fallback, and the Solution Architect can generate new overlays on demand.

## Enforcement Hooks

Quality isn't requested — it's enforced structurally. 8 Python hooks run automatically on Claude Code lifecycle events:

| Hook | What It Does |
|---|---|
| `block-git-commit` | Blocks commits unless Tech Lead gate is approved, DoD checklist complete, tests pass |
| `block-destructive-ops` | Blocks `rm -rf /`, `DROP TABLE`, force push to main, and other dangerous commands |
| `validate-file-scope` | Blocks agents from writing outside their permitted file scope |
| `run-linter` | Runs stack-appropriate linter after every file edit |
| `log-file-changes` | Logs every file modification to the pipeline audit trail |
| `handoff-gate` | Writes gate files and sends desktop notifications when agents complete |
| `enforce-dod` | Validates Definition of Done before allowing task completion |
| `collect-output` | Aggregates subagent output into the pipeline log |

## External Integrations

| Tool | Purpose | Used By |
|---|---|---|
| [MCP Atlassian](https://github.com/sooperset/mcp-atlassian) | Jira stories + Confluence docs (72 tools) | Scrum Master, Technical Writer, Security, Tech Lead, QA |
| [Playwright MCP](https://github.com/microsoft/playwright-mcp) | Browser-based acceptance testing | QA Engineer |
| [UI UX Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | Design system generation (161 rules, 67 styles) | UX Designer |

## Brownfield Support

For existing codebases, Stagix automatically activates brownfield mode:

1. **Codebase Archaeologist** produces a 12-section discovery report before any planning begins
2. All planning agents read the discovery report as their first input
3. Stories include regression risk, rollback procedures, and feature flag recommendations
4. Regression baselines are captured before each epic
5. Compatibility checks validate backward compatibility before code review

## Project Structure

```
.stagix/                          Plugin root
├── .claude-plugin/plugin.json    Manifest (agents, commands, hooks, MCP)
├── agents/
│   ├── planning/                 9 planning agents
│   └── engineering/              8 engineering agents
├── commands/                     7 slash commands
├── skills/                       12 domains, 69 stack overlays
├── hooks/                        8 Python enforcement scripts
├── templates/                    18 YAML document blueprints
├── checklists/                   8 quality gate validators
├── workflows/                    6 end-to-end workflow definitions
├── modes/                        greenfield.yaml, brownfield.yaml
├── tasks/                        13 execution protocols
├── gates/                        Runtime gate files (human approval)
├── state/                        Runtime pipeline state
├── core-config.yaml              Runtime configuration
├── .env.example                  Credential template
└── install.sh                    Shell installer
```

## How It Compares

| | Traditional AI Coding | Stagix |
|---|---|---|
| **Agents** | 1 generalist | 14 specialists with tool boundaries |
| **Requirements** | Assumed from prompt | 5-phase structured elicitation |
| **Architecture** | Invented on the fly | Designed, reviewed, approved before code |
| **Security** | Hope for the best | Dedicated OWASP audit, blocks on CRITICAL/HIGH |
| **Tests** | Written by the same agent that wrote the code | Written by a specialist BEFORE implementation |
| **Code Review** | None | 5-dimension review (quality, security, tests, architecture, performance) |
| **QA** | None | Browser-based Playwright testing against running app |
| **Audit Trail** | Git log | Jira lifecycle + Confluence docs + gate files |
| **Human Control** | Conversational | Deterministic file-based gates at every boundary |

## Acknowledgements

Inspired by the [BMAD Method](https://github.com/bmadcode/bmad-method) (v4.44.3). Stagix builds on BMAD's philosophical foundation while adding automated orchestration, MCP integration, hook enforcement, and the plugin architecture.
