# Migration Standards — Universal Principles

## Zero-Downtime Migration Strategy
1. **Add** new column (nullable, no default)
2. **Deploy** code that writes to both old and new columns
3. **Backfill** existing rows
4. **Deploy** code that reads from new column only
5. **Drop** old column

Never do steps 1-5 in a single deployment.

## Migration Safety Rules
- Every migration must be reversible (down migration defined)
- Never rename columns in production (add new → migrate → drop old)
- Never change column types without a multi-step migration
- Test migrations against production-volume data (not empty tables)
- Idempotent: running the same migration twice must not error

## Rollback Safety
- Every migration has a tested rollback procedure
- Rollbacks must not lose data
- If rollback is impossible (data transformation), document this clearly

## Index Management
- Create indexes CONCURRENTLY where supported (non-blocking)
- Don't create indexes in the same migration as data changes
- Large table indexes: estimate creation time, schedule during low traffic

## Data Migrations vs Schema Migrations
- Keep them separate: schema in migration files, data in scripts
- Data migrations are one-time scripts, not repeatable migrations
- Log data migration progress (for large tables, report every N rows)
