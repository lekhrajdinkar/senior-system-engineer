# Shortest Path Algorithms
## reference
- https://www.hellointerview.com/learn/code/graphs/shortest-path-algorithms

## Overview
![img_1.png](img_1.png)

---
## 1. BFS
**When to Use BFS**
- Grid navigation (moving up/down/left/right)
- Unweighted graph traversal | can assume, weight is 1 for all edges
- Finding **minimum** number of steps/moves

> [03_09_BFS](../03_Problems/03_09_BFS)

---
## 2. Dijkstra's Algorithm
**When to Use Dijkstra**
- Weighted graphs with non-negative edges
- Finding shortest path from one source to all nodes
- Problems involving "minimum cost" or "minimum time"