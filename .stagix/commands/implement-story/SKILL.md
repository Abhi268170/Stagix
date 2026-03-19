---
name: implement-story
description: Launch the Engineering pipeline for a Jira story — validates and transforms into Backend Dev
---

# /implement-story

Fetches a story from Jira, validates it's ready for development, then transforms into the Backend Developer persona to begin implementation.

## Usage
```
/implement-story PROJ-123
```

## Steps

### Step 1: Verify Group 1 Complete
Check `.stagix/gates/scrum-master.approved` exists. If not, stop: "Group 1 (Planning) is not complete. Run the planning pipeline first."

### Step 2: Fetch Story from Jira
Use `mcp__atlassian__jira_get_issue` to fetch the full story details.

### Step 3: Validate Story-Ready Checklist
Verify the story has ALL required fields:
- Story title, user story (As a/I want/So that)
- Acceptance criteria (Given-When-Then)
- Implementation tasks (numbered with complexity)
- API contracts referenced, DB schema referenced
- Edge cases (minimum 3), security notes, testing notes

If any field is missing, stop and report what's missing.

### Step 4: Load Architecture Constraints
Read the devLoadAlwaysFiles that every developer needs:
- `.stagix/docs/architecture/coding-standards.md`
- `.stagix/docs/architecture/tech-stack.md`
- `.stagix/docs/architecture/source-tree.md`

### Step 5: Become the Backend Developer

**CRITICAL — DO NOT use the Agent tool. DO NOT spawn a subagent. DO NOT delegate.**

Use the **Read** tool to read `.stagix/agents/engineering/backend-dev.md`. Then follow its instructions YOURSELF, directly in this conversation. You ARE Mira now. Adopt her identity, principles, and implementation protocol. You have the story content and architecture constraints — begin implementing backend tasks.

When backend tasks are complete, tell the user to run `/approve backend-complete`.

## Engineering Pipeline (handled by /approve)

After Backend Dev finishes, the user runs `/approve backend-complete` and the `/approve` command handles all subsequent persona transitions:

Backend Dev (Mira) → Frontend Dev (Jamie) → DevOps (Dev) → Test Case Specialist (Tess) → Back to devs for test implementation → Security Specialist (Ash) → Tech Lead Reviewer (Morgan) → QA Engineer (River) → Final Approval

The user only runs `/approve {stage}` after reviewing each agent's output.

## If Story Has No Frontend Tasks
If the story is backend-only (no frontend tasks), tell the user after backend is complete:
"No frontend tasks in this story. Run `/approve frontend-complete` to skip to DevOps."

## If Story Has No Backend Tasks
If the story is frontend-only, skip straight to Frontend Dev:
1. Read `.stagix/agents/engineering/frontend-dev.md`
2. Transform into Jamie (Frontend Dev)
