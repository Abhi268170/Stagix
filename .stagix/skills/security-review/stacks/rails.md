# Ruby on Rails Security

## Stack-Specific Risks
- Mass assignment: strong_parameters always
- SQL injection via raw SQL or find_by_sql with interpolation
- CSRF: verify_authenticity_token on all controllers
- Deserialization: avoid YAML.load (use YAML.safe_load)
- File access: sanitize file paths, no user-controlled paths
