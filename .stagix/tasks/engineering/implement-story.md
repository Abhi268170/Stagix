# Task: implement-story

## Purpose

Dev's sequential task execution protocol with blocking conditions. Governs how Backend Dev and Frontend Dev implement each task in a story.

## Protocol

### For Each Task in the Story (in order)

```
1. READ the task description
   - Identify referenced API contract section
   - Identify referenced DB schema section
   - Understand the acceptance criteria this task contributes to

2. CHECK project structure
   - Read source-tree.md to know where files go
   - Check if files to modify already exist

3. IMPLEMENT
   - Write code following coding-standards.md
   - Place files per source-tree.md
   - Use tech-stack.md versions exactly
   - Follow existing codebase patterns

4. WRITE TESTS
   - Unit tests for the implementation
   - Follow testing framework conventions
   - Cover happy path + edge cases from the story
   - Tests must be self-contained

5. RUN TESTS
   - Execute: stack-appropriate test command
   - ALL tests must pass (new AND existing)
   - If tests fail: fix and re-run (up to 3 attempts)
   - If 3 failures: escalate to human

6. UPDATE STORY RECORD
   - Mark task checkbox [x]
   - Add to File List: every new/modified file
   - Add to Change Log: what was implemented
   - Add to Dev Agent Record: implementation notes

7. NEXT TASK
   - Move to next numbered task
   - Do not skip or reorder
```

## Blocking Conditions

STOP execution and escalate if:

| Condition | Action |
|---|---|
| Unapproved dependency needed | Ask human: "This requires {package} not in tech-stack.md" |
| Ambiguity after re-reading story | Ask human: "Story says X but architecture says Y" |
| 3 consecutive test failures on same task | Escalate: "Task {N} failing after 3 attempts: {error}" |
| Missing config/env values | Ask human: "Need {value} — not in environment" |
| File outside permitted scope | STOP: "Task requires modifying {file} outside my scope" |

## Story File Permissions

Developers may ONLY modify:
- Task checkboxes (mark [x])
- Dev Agent Record section
- File List section
- Change Log section
- Status field

Developers may NOT modify:
- Story text, AC, or Testing sections
- Security Notes
- Edge Cases

## Re-Spawn for Test Implementation

When re-spawned after Test Case Specialist produces test plan:
1. Read `.stagix/tests/{story-key}-test-plan.md`
2. Implement EXACTLY these test cases — do not modify, skip, or add extras
3. Run all tests
4. Report pass/fail results
