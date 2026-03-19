# Java Security

## Stack-Specific Risks
- Deserialization: never deserialize untrusted data (ObjectInputStream)
- XXE: disable external entities in XML parsers
- SQL injection: use PreparedStatement, never concatenate
- Spring Security: verify filter chain ordering
- Log injection: sanitize user input before logging
