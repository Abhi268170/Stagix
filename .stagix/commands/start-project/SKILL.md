---
name: start-project
description: Launch the Stagix Planning pipeline for a new project or feature
---

# /start-project

Launches the Stagix planning pipeline by detecting the tech stack and activating the Business Analyst for interactive requirements elicitation.

## Usage
```
/start-project "A SaaS project management tool for small teams"
```

## Steps

### Step 1: Detect Stack
Read signal files in the project root to determine tech stack and mode:
- package.json → Node.js/React/Vue/etc.
- requirements.txt / pyproject.toml → Python/FastAPI/Django/etc.
- go.mod, Gemfile, Cargo.toml, etc.
- Existing source files → brownfield mode

Update `.stagix/core-config.yaml` with `detected_stack` and `mode` (greenfield/brownfield).

### Step 2: Brownfield Discovery (if applicable)
If mode is brownfield, tell the user:
```
Brownfield mode detected. Run the Codebase Archaeologist first:
  Activate the codebase-archaeologist agent
  After it completes, run: /approve discovery
  Then re-run: /start-project "your idea"
```
Stop here for brownfield — the user needs to run discovery first.

### Step 3: Activate Business Analyst
For greenfield (or after brownfield discovery is approved):

Tell the user to activate the Business Analyst agent directly. The BA needs to run as the main thread to have an interactive multi-turn conversation.

```
Stack detected. Planning pipeline ready.

Next step — activate the Business Analyst:
  Use the business-analyst agent with your project idea.

The BA will conduct a 5-phase interactive elicitation to build your project brief.
After the BA completes, run: /approve business-analyst
```

## Important
Do NOT spawn subagents or activate a Planning Lead orchestrator. Planning agents run one at a time as the main thread because they need interactive conversations with the user. The gate system (/approve, /reject) sequences them.

## Full Planning Sequence
Each agent runs as main thread, one at a time:

1. **Business Analyst** (Priya) — interactive elicitation → `/approve business-analyst`
2. **Product Manager** (Nate) — PRD from brief → `/approve product-manager`
3. **UX Designer** (Lena) — UX spec + design system → `/approve ux-designer`
4. **Solution Architect** (Soren) — architecture + sharded docs → `/approve solution-architect`
5. **Database Designer** (Rex) — schema + migrations → `/approve db-designer`
6. **Technical Writer** (Alex) — Confluence publishing → `/approve technical-writer`
7. **Scrum Master** (Kai) — Jira epics + stories → `/approve scrum-master` (unlocks Group 2)
