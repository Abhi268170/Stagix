# DynamoDB

## Specifics
- Single-table design (GSIs for access patterns)
- Partition key selection: high cardinality, even distribution
- Sort key for range queries within a partition
- GSI overloading for multiple access patterns
- DynamoDB Streams for change data capture
- On-demand capacity for unpredictable workloads
