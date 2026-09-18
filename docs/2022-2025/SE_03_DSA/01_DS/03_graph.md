# Graph 
## Overview
[04_graph.excalidraw](../draw/03/07_DFS/04_graph.excalidraw)

- Graphs consist of **nodes** (also frequently referred to as vertices), and **edges** that connect the nodes.
- graphs can be either directed or undirected.
- Nodes that are connected to each other via an edge are known as the **neighbors** of that node.
- A graph can contain **cycles**| A cycle is a path that starts and ends at the same node.
- A **connected graph** is a graph where there is a path between every pair of nodes
- A **disconnected graph** is a graph where there are at least two nodes that are not connected to each other by a path.
> 💡A tree is a connected graph with no cycles

---
## representations
adjacency lists

2d matrices

```Direction

(r, c) = node

        (r-1,c)
           ↑
(r,c-1) ← (r,c) → (r,c+1)
           ↓
        (r+1,c)
```
