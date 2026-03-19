# PostgreSQL

## Specifics
- JSONB for semi-structured data (not JSON — JSONB is indexable)
- GIN indexes for JSONB and full-text search
- CTEs for complex queries (readable > clever)
- LISTEN/NOTIFY for real-time triggers
- Partial indexes for filtered queries
- pg_stat_statements for query performance monitoring
- Connection pooling via PgBouncer
