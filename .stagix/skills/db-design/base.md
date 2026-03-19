# Database Design — Universal Principles

## Normalisation
- Start with 3NF — denormalise only with measured justification
- Every table has a primary key (prefer UUID or ULID over auto-increment for distributed systems)
- Foreign keys enforced at DB level, not just application level
- No data duplication without explicit denormalisation rationale

## Indexing Principles
- Every foreign key column gets an index
- Every column in a WHERE clause used frequently gets an index
- Composite indexes: put the most selective column first
- Don't over-index: each index slows writes
- Justify every index with a specific query pattern

## N+1 Avoidance
- Design queries to fetch related data in one round trip
- Use JOINs or subqueries, not sequential queries in a loop
- ORM eager loading configured for known access patterns

## Migration Safety
- Migrations are ordered, idempotent, and reversible
- Never rename a column in production — add new, migrate data, drop old
- Never drop a column without a deprecation period
- Add columns as nullable first, then backfill, then add constraints
- Test migrations against a copy of production data volume

## Data Integrity
- NOT NULL where data is required (don't rely on app validation alone)
- CHECK constraints for enum-like values
- UNIQUE constraints where business rules require it
- Timestamps: created_at (auto), updated_at (auto), deleted_at (soft delete if needed)
