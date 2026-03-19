# Flyway (JVM)

## Conventions
- Versioned migrations: V{version}__{description}.sql
- Repeatable migrations: R__{description}.sql for views/functions
- Baseline for existing databases
- Clean only in dev (never production)
