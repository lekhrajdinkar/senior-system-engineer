# CAP theorem

> A distributed system can only guarantee two of the three properties: 
**Consistency**, **Availability**, and **Partition tolerance**.
> 
> CAP is NOT: “Pick two and ignore the third”
> 
> CAP IS: “When partition happens, you must choose between C and A”

## Network Partition
- This occurs when a network failure (temporary and permanent)
- divides a distributed system into isolated parts, 
- preventing communication between them.
- This is an unavoidable fact in distributed systems
- Single Node server, has No Partition :)

> A network partition is not an anomaly that stops a distributed system from being distributed; 
rather, it's a common and expected challenge that distributed systems are designed to handle, 
by choosing how they will prioritize **consistency** or **availability** during such an event.

## Concept overview
✔️Partition Tolerance (P)
- Ability to continue operating despite network failure
- in reality all DS continue to work, even if network fails (**between nodes**)
- so P is mandatory

✔️Consistency (C) 
- Ensures that all nodes in a distributed system have the same, most up-to-date data. 
- If there's a partition, the system will not allow any actions until the network is restored, 
- guaranteeing 100% accurate data.

✔️Availability (A) 
- Ensures that the system remains operational and responsive even if some data is inconsistent or stale.
- The system will accept actions and process them later once the network is restored, 
- providing "eventual consistency."

## CAP Model (2) - CP or AP
```
- P Partition tolerance is "mandatory"
- we're really choosing between:
  - CP → correctness first
  - AP → uptime first
- CA is a fantasy outside of single-node systems
```

## Understand by Example
- Two nodes, replicating data, serving users.
- Network partition occurs
  - Node1 and Node2 cannot talk **to each other**.
  - but still server user === P
- During partition, you must choose:
  - **Option A**: AP (`Availability` + Partition Tolerance)
    ```
    Node1 serves users
    Node2 serves users
    Both are “available”
    Data may diverge
    
    User writes X=10 to node1
    User reads X from node2 → gets old value X=5
    ```
  - Option B: CP (`Consistency` + Partition Tolerance)
    ```
    One node (or both) refuses requests
    Leader election may fail
    Writes may be blocked
    
    Node1: "I can’t confirm with node2 → I reject the write"
    Node2: "Same here
    ```

---
## Real world scenarios

| System            | Consistency | Availability | Partition Tolerance | CAP Type |
| ----------------- | ----------- | ------------ | ------------------- | -------- |
| **Kafka**         | ✅           | ❌            | ✅                   | **CP**   |
| **Aurora Global** | ❌           | ✅            | ✅                   | **AP**   |
| **DynamoDB**      | ❌ (default) | ✅            | ✅                   | **AP**   |


