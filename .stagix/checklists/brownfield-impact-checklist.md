# Brownfield Impact Checklist

Validates backward compatibility before code review.

## API Compatibility
- [ ] No existing endpoint signatures changed
- [ ] No response fields removed/renamed
- [ ] New optional fields truly optional
- [ ] Error format unchanged

## Schema Compatibility
- [ ] No columns removed/renamed
- [ ] New columns nullable or have defaults
- [ ] Migrations reversible
- [ ] No indexes dropped

## Config Compatibility
- [ ] No existing env vars removed
- [ ] New env vars have defaults

## Dependency Compatibility
- [ ] No packages downgraded
- [ ] No packages removed that existing code uses
