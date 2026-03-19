# Task: story-dod-check

## Purpose

Developer self-check before marking story complete. Maps to the enforce-dod.py hook validation. If you pass this checklist, the hook will allow task completion.

## Definition of Done Checklist

### 1. Requirements Met
- [ ] All functional requirements for this task are implemented
- [ ] All acceptance criteria from the story are addressed
- [ ] Edge cases from the story are handled in code

### 2. Coding Standards & Project Structure
- [ ] Code follows coding-standards.md conventions
- [ ] Files placed per source-tree.md
- [ ] Tech stack versions match tech-stack.md
- [ ] API implementations match api-contracts.md
- [ ] Data models match db-schema.md
- [ ] No linting errors (run-linter.py should have caught these)

### 3. Testing
- [ ] Unit tests written for new code
- [ ] Integration tests written where applicable
- [ ] All tests pass (new AND existing)
- [ ] Coverage meets threshold from core-config.yaml

### 4. Functionality & Verification
- [ ] Manually verified the implementation works
- [ ] Edge cases tested
- [ ] Error handling produces user-friendly messages

### 5. Story Administration
- [ ] All task checkboxes marked [x]
- [ ] File List updated with every new/modified file
- [ ] Change Log updated
- [ ] Dev Agent Record filled (model, notes, completion status)

### 6. Dependencies, Build & Configuration
- [ ] Build completes without errors
- [ ] All linting passes
- [ ] No new dependencies added without approval
- [ ] No hardcoded secrets or credentials

### 7. Documentation
- [ ] Non-obvious code has inline comments
- [ ] Public APIs have documentation
- [ ] Any new environment variables documented in .env.example
