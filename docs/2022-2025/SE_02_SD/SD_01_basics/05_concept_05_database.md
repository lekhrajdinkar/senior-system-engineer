# Database SD concept
## ✔️Data Consistency
levels of consistency
- Strong
- eventual

## ✔️Replication
### Overview
- https://www.youtube.com/watch?v=CSCw16AfWHM
- key role in designing high-performing systems
- core idea - create multiple copies of a database
  - to ensure system **availability** 
  - and improve **performance**
    - by placing replicas closer to users in different geographical regions 👈🏻

**Synchronous Replication** 
- Ensure that writes to the main database are **immediately** reflected in the replica.
- This guarantees data consistency but can **increase write operation time**.

**Asynchronous Replication**
> ℹ️Read replication
- Allow the main database to update the replica at later, 
- consistent intervals (e.g., every minute or five minutes).
- This speeds up write operations on the main database 
- but may result in a slight delay for data consistency across replicas === eventual consistent

---
## ✔️DB Scaling - Sharding
**vertical Scale**
- making a single server more powerful
- but limited

**Horizontal scale**
- splitting the main database into smaller, independent databases called **shards** or data partitions
- crucial consideration when sharding is **avoiding data hotspots**
  - mitigate : **hashing** is a reasonable way to split data uniformly

---
## ✔️Relational vs Non_relational
Relation
- offer powerful querying capabilities due to their structured nature
- https://www.youtube.com/watch?v=6bZdMZb8xI8
- https://github.com/lekhrajdinkar/data-engineer/tree/main/docs/2012-2021 👈🏻👈🏻

Non_relational
- [check here](05_concept_06_noSql.md)







