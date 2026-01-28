# client-server architecture
- dns concept
- http 80 | https  8443
- `nslookup` command
- ...

---
## Polling
- https://www.youtube.com/watch?v=b4qyOpGg748
- client repeatedly requests data from a server at set intervals.
- eg:
  - Temperature Monitoring
  - not ideal for real-time applications like chat
- **reducing** the polling interval
  -  it significantly increases the **load on the server**, 
  - as clients send many **unnecessary requests**.
  
> ℹ️ suitable for data that doesn't **need to be updated very frequently**

---
## Streaming
- https://www.youtube.com/watch?v=b4qyOpGg748
- the client opening a **long-lived connection** with the server, 
- typically through a **socket**, 
- allowing the server to **push** information **without a client request**

> ℹ️ **instantaneous experiences**
> - the server proactively sends or "pushes" data to the client, 
> - rather than passively waiting for requests.
> - Enables a **continuous flow of data**

---
## Pub-Sub 
(kafka is popular tool) 👈🏻
> **At Least Once Delivery**
>   - subscriber receives a message but loses connection before acknowledging it.
>   - leading the topic to re-send the message when the connection is re-established
>   - **idempotent operation** yields the same outcome regardless of how many times it's performed
> 
> **Message Ordering** : "first-in, first-out" (FIFO)
> 
> **Message Replay**, due to their underlying persistent storage

### Components
**Publishers:** 

**Topics:** 
- Act as channels or intermediaries with specific information.
- Persistent Storage via Topic

**Subscribers:** 
- Clients that listen for data from topics.
- can subscribe to multiple topics based on their needs.
- Unlike streaming, subscribers listen to the topic, not directly to the publishers

**Messages**: 
- Represent data or event

### More
-  **separation of concern**.
- **Contend based filter**


