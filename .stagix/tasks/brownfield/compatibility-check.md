# Task: compatibility-check

## Purpose

Validates new code doesn't break existing APIs or database schema. Runs before code review in brownfield mode.

## Checks

### 1. API Backward Compatibility
- [ ] No existing endpoint signatures changed (method, path, required params)
- [ ] No existing response shapes changed (fields not removed or renamed)
- [ ] New optional fields are truly optional (existing clients unaffected)
- [ ] Error response format unchanged
- [ ] No existing status codes changed in meaning

### 2. Database Schema Compatibility
- [ ] No columns removed or renamed
- [ ] No column types changed
- [ ] New columns are nullable OR have defaults
- [ ] No indexes dropped
- [ ] Foreign key changes don't orphan existing data
- [ ] Migrations are reversible

### 3. Configuration Compatibility
- [ ] No existing environment variables removed or renamed
- [ ] New environment variables have defaults or are optional
- [ ] No existing config file format changes

### 4. Dependency Compatibility
- [ ] No existing package versions downgraded
- [ ] No packages removed that existing code depends on
- [ ] New packages don't conflict with existing ones

## Output

PASS if all checks clear. FAIL with specific incompatibilities listed. FAILs must be resolved before proceeding to code review.
