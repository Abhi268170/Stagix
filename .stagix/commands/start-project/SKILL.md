---
name: start-project
description: Launch the Stagix Planning Collective for a new project or feature
---

# /start-project

Launches the full Stagix planning pipeline.

## Usage
```
/start-project "A SaaS project management tool for small teams"
```

## What Happens
1. Run detect-stack: Read signal files, determine tech stack and mode (greenfield/brownfield)
2. Write detected stack to `.stagix/core-config.yaml`
3. If brownfield mode: Activate Codebase Archaeologist first, wait for discovery gate
4. Activate Planning Lead agent with the project idea
5. Planning Lead orchestrates the full Group 1 sequence

## Arguments
- First argument: The project idea/description (in quotes)

## Prerequisites
- `.stagix/` directory installed (run install.sh first)
- Jira and Confluence credentials configured in `.stagix/.env`
