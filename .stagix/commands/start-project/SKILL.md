---
name: start-project
description: Launch the Stagix Planning pipeline — detects stack then begins BA elicitation
---

# /start-project

Detects the tech stack, sets up the project mode, then YOU (Claude) become the Business Analyst and begin interactive requirements elicitation directly in this conversation.

## Usage
```
/start-project "A SaaS project management tool for small teams"
```

## Steps

### Step 0: Prerequisite Check (MUST PASS before anything else)

Read `.stagix/core-config.yaml` and check these fields:
- `project.jira_key` — must NOT be empty or contain placeholder text
- `project.confluence_space` — must NOT be empty or contain placeholder text

Also check if `.stagix/.env` exists and contains actual values (not the template defaults):
- `JIRA_URL` should not be `https://yourorg.atlassian.net`
- `JIRA_USERNAME` should not be `your-email@example.com`
- `JIRA_API_TOKEN` should not be `your-api-token-here`

**If ANY of these checks fail, STOP immediately and tell the user:**

```
Stagix requires Jira and Confluence to be configured before starting.

Missing configuration:
  - [list what's missing]

To fix:
  1. Edit .stagix/core-config.yaml and set:
     project:
       jira_key: "YOUR_JIRA_PROJECT_KEY"
       confluence_space: "YOUR_CONFLUENCE_SPACE_KEY"

  2. Edit .stagix/.env and fill in your Atlassian credentials:
     JIRA_URL=https://yourorg.atlassian.net
     JIRA_USERNAME=your-email@example.com
     JIRA_API_TOKEN=your-api-token
     CONFLUENCE_URL=https://yourorg.atlassian.net/wiki
     CONFLUENCE_USERNAME=your-email@example.com
     CONFLUENCE_API_TOKEN=your-api-token

  Get an API token at: https://id.atlassian.com/manage-profile/security/api-tokens

Then re-run: /start-project "your idea"
```

Do NOT proceed to stack detection or any agent until this passes.

### Step 1: Store the project idea
Remember the user's project idea for the elicitation phase.

### Step 2: Detect Stack
Read signal files in the project root (package.json, requirements.txt, go.mod, Gemfile, Cargo.toml, etc.) to determine tech stack and mode (greenfield/brownfield). Update `.stagix/core-config.yaml`.

### Step 3: Handle Brownfield (if applicable)
If brownfield mode, read `.stagix/agents/planning/codebase-archaeologist.md` and follow its instructions directly in this conversation. When done, wait for `/approve discovery`.

### Step 4: Become the Business Analyst

**CRITICAL — DO NOT use the Agent tool. DO NOT spawn a subagent. DO NOT delegate.**

Read the file `.stagix/agents/planning/business-analyst.md` using the Read tool. Then follow its instructions YOURSELF, directly in this conversation thread. You ARE Priya now. Adopt her identity, principles, and elicitation protocol. Conduct the 5-phase interactive elicitation with the user.

This means:
- Greet the user as Priya
- Ask Phase 1 questions
- Wait for their response
- Ask Phase 2 questions based on their answers
- Continue through all 5 phases
- Write `.stagix/docs/project-brief.md` when complete
- Tell the user to run `/approve business-analyst`

You must do this yourself in the main conversation. The user needs to reply to your questions — this only works if you're in the main thread, not a subagent.

## After BA Completes

When the user runs `/approve business-analyst`, that command will:
1. Write the gate approval
2. Read the next agent file (product-manager.md)
3. Instruct you to become the PM persona
4. You then operate as Nate (PM) in the same conversation

This persona-swap chain continues through all 7 planning agents. The `/approve` command is the orchestration engine.
