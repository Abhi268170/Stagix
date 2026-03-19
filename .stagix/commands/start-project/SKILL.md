---
name: start-project
description: Launch the Stagix Planning pipeline — detects stack and transforms into the Business Analyst
---

# /start-project

Detects the tech stack, sets up the project mode, then transforms into the Business Analyst persona to begin interactive requirements elicitation.

## Usage
```
/start-project "A SaaS project management tool for small teams"
```

## Steps

### Step 1: Store the project idea
Save the user's project idea — it will be passed to the Business Analyst.

### Step 2: Detect Stack
Read signal files in the project root to determine tech stack and mode:
- package.json → Node.js/React/Vue/etc.
- requirements.txt / pyproject.toml → Python/FastAPI/Django/etc.
- go.mod, Gemfile, Cargo.toml, etc.
- Existing source files → brownfield mode

Update `.stagix/core-config.yaml` with `detected_stack` and `mode` (greenfield/brownfield).

### Step 3: Handle Brownfield (if applicable)
If mode is brownfield:
1. Read `.stagix/agents/planning/codebase-archaeologist.md`
2. Transform into Sam (Archaeologist)
3. Execute the discovery protocol
4. When complete, present the discovery report and wait for `/approve discovery`
5. After approval, proceed to Step 4

### Step 4: Transform into Business Analyst
1. Read `.stagix/agents/planning/business-analyst.md`
2. Adopt Priya's identity, role, principles, and instructions completely
3. Begin the 5-phase interactive elicitation with the user's project idea
4. Stay in the BA persona until the project brief is complete

## CRITICAL: Persona Swap Pattern

This command starts the chain. After the BA finishes:
- The user runs `/approve business-analyst`
- The `/approve` command reads the next agent file and transforms into that persona
- This continues through all 7 planning agents automatically

The user only needs to:
1. `/start-project "idea"` — starts the chain
2. Interact with each agent as needed
3. `/approve {stage}` — after reviewing each agent's output
4. `/reject {stage} "feedback"` — if changes are needed

The `/approve` command handles all persona transitions. No manual agent switching needed.
