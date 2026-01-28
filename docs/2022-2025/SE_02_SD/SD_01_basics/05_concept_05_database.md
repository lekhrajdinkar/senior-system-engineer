# Database SD concept
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
> Read replication
- Allow the main database to update the replica at later, 
- consistent intervals (e.g., every minute or five minutes).
- This speeds up write operations on the main database 
- but may result in a slight delay for data consistency across replicas === eventual consistent

---
## ✔️DB Scaling

---
## ✔️ACID

---
## ✔️NoSQL DB
