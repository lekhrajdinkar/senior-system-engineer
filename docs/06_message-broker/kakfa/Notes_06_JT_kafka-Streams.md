# Kafka Streams

## A. Intro
- **Scenario**: 
  - bank-txn-topic > event/txn are published here > if txn amt>500 for customer-1 > sent alert + create alert dashboard.
  - note: consumer are stateless, know only current event, not previous event.
- sol-1 (manual, messy)
  - track thing on DB + CRUD
  - load on cache (for performance)
  - custom logic to filter, aggr, map, etc
  - more: handle scaling, thread safety, handel offset, etc
- sol-2 (use kafka Stream processing API) 👈🏻
  - high level (**DSL**) 
    - Declarative style, less code, easy
    - `StreamBuilder`, `KStream`, `KTable`
  - low level (**processor api**)
    - more control
    - but more boilerplate code

---
## B. Simple Consumer vs StreamProcessApp

- Architectural Rule of Thumb 👍🏻👍🏻
    - Microservice logic → Consumer API
    - Data pipeline logic → Kafka Streams
  
| Aspect          | Simple Consumer | Kafka Streams |
| --------------- | --------------- | ------------- |
| Abstraction     | Low-level       | High-level    |
| State           | Manual          | Built-in      |
| Offset handling | Manual          | Automatic     |
| Scaling         | Your problem    | Automatic     |
| Exactly-once    | Hard            | Native        |
| Windowing       | Manual          | Native        |
| Joins           | Manual          | Native        |
| External calls  | Easy            | Risky         |
| Debugging       | Easier          | Harder        |

- **Kafka Consumer API** (`Low-level`)
  - We manage everything:
    - manually poll, deserialize, process, and commit offsets
    - Retry logic, Error handling, Threading & backpressure
    - Stateless by default (state handling is our responsibility)
  - **cons**:
    - Scaling & rebalancing complexity
    - Error-prone offset handling
  - **Best use case**:
    - Event-driven microservices
    - Transactional workflows
    
```java
while (true) 
{
    ConsumerRecords<String, String> records = consumer.poll(Duration.ofMillis(100));
    for (ConsumerRecord<String, String> record : records) {
        process(record.value());
    }
    consumer.commitSync();
}    
```

- Kafka StreamProcessorApp (High-level)
  - Built on top of Kafka consumer & producer APIs
  - Built-in : State stores, Windowing, Joins, Aggregations, Repartitioning
  - Fault-tolerant via changelog topics
  - Exactly-once semantics
  - Flow: **Topic → Stream → Transform → Aggregate/Join → Output Topic** 🔸
  - **cons**:
    - Harder debugging 
    - Not ideal for heavy external I/O
  - **Best use cases**:
    - Real-time analytics
    - Event enrichment
    - Stateful transformations
    - Stream joins (KStream-KStream, KTable)


---
## C. System Design Example   
## C.1 Real-Time Fraud Detection App (JT)
- Kafka Streams + Spring Boot + Java21
- https://www.youtube.com/watch?v=U7RZcBtP6Dw&list=PLVz2XdJiJQxz55LcpHFM6QIB-Px40w3Gt&index=4
- ![img.png](temp/06/01/img.png)

### C.2 from chatGPT-5.2
#### HLD
```declarative
[ Kafka Topic: orders ]
    |
    v
[ Kafka Streams App (Spring Boot) ]
- filter invalid events
- map (parse JSON)
- group by customerId
- aggregate totalAmount
    |
    v
[ Kafka Topic: customer-order-totals ]

```
- Key Characteristics
  - Stateless + stateful processing
  - Uses embedded **RocksDB** state store
  - Exactly-once capable (configurable)
  - **Horizontally scalable** via Kafka partitions
  - fault tolerance