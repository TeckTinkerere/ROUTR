# routr-database boundaries

| Situation | Use instead |
|-----------|-------------|
| ORM or client-library setup only, no schema/query work | `routr-integrate` |
| Query bug with unknown root cause | `routr-debug` |
| Full security audit beyond RLS (authN/authZ, secrets, CVEs) | `routr-security` |
| Shipping the migration once written | `routr-ship` |
