# Graph: Shortest Path Algorithms
## reference
- https://www.hellointerview.com/learn/code/graphs/shortest-path-algorithms

## Overview
shortest path from one source node to all other nodes

![img_1.png](../../../99_img/2026/hi/dsa/11/01/img_1.png)

---
## 1. BFS
> [BFS-on-graph.md](../03_Problems/03_09_BFS/02_01_BFS-on-graph.md)

### When to Use
- Grid navigation (moving up/down/left/right)
- Unweighted graph traversal | can assume, weight is 1 for all edges
- Finding **minimum** number of steps/moves

### visual 
[03_bfs-shortest-path.excalidraw](../draw/03/10_graph_more/03_bfs-shortest-path.excalidraw)

![img_3.png](../../../99_img/2026/hi/dsa/11/01/img_3.png)

### Algo
@[code:section::short_path_bfs,util-1](../../../../src/leetcode/hellointerview/graph/Exercise-2.py)

**Complexity**
- `O(V + E)` | space
- `O(V + E)` | time

---
## 2. Dijkstra's Algorithm 
### When to Use
- Weighted graphs with **non-negative** edges
- Finding the **shortest path** from one source to all nodes
- Problems involving **"minimum cost" or "minimum time"**

### visual
[02_Dijkstra.excalidraw](../draw/03/10_graph_more/02_Dijkstra.excalidraw)

![img_2.png](../../../99_img/2026/hi/dsa/11/01/img_2.png)

---
### Algo
@[code:section::short_path_dijkstra,short_path_dijkstra_2,util-1](../../../../src/leetcode/hellointerview/graph/Exercise-2.py)

**Complexity:**
- `O((V + E) log V)` | time
  - V = number of nodes
  - E = number of edges
  - heap push/pop = `O(log V)`
- `O(V + E)` | space


