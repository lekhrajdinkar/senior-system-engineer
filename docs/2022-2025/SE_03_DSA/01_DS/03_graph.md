# Graph 
## Graph :: Overview
[04_graph.excalidraw](../draw/03/07_DFS/04_graph.excalidraw)

- Graphs consist of **nodes** (also frequently referred to as vertices), and **edges** that connect the nodes.
- graphs can be either directed or undirected.
- Nodes that are connected to each other via an edge are known as the **neighbors** of that node.
- A graph can contain **cycles**| A cycle is a path that starts and ends at the same node.
- A **connected graph** is a graph where there is a path between every pair of nodes
- A **disconnected graph** is a graph where there are at least two nodes that are not connected to each other by a path.
> 💡A tree is a connected graph with no cycles

---
## Representations of graph
### adjacency lists

```adjList
# ==================================
# unweighted graph, un-directed 👈
# ==================================
adjList = 
{
  0: [1, 3, 2],
  1: [0, 2],
  2: [1, 3, 0],
  3: [2, 0]
}

# ==================================
# weighted graph 👈
# ==================================

adjList2 = {
    "A": [("B", 4), ("C", 2)],
    "B": [("A", 4), ("D", 1)],
    "C": [("A", 2), ("D", 3)],
    "D": [("B", 1), ("C", 3)]
}
```

### 2d matrices

```2d
# unweighted graph, un-directed 👈
 grid = [
            [1, 0, 1],      
            [1, 0, 0],
            [0, 0, 1]
      ]

```

```neighbors
(r, c) = node, is refrered by coordinates
neighbours are  coordinates shift in 4 direction

        (r-1,c)
           ↑
(r,c-1) ← (r,c) → (r,c+1)
           ↓
        (r+1,c)
```

---
## Graph problems
- [DFS_on_graph.md](../03_Problems/03_08_DFS/03_01_DFS_on_graph.md)
- [BFS-on-graph.md](../03_Problems/03_09_BFS/02_01_BFS-on-graph.md)
- [01_03_topological-sort.md](../02_Algo/01_03_topological-sort.md)
- [02_shortest-path-algos.md](../02_Algo/02_shortest-path-algos.md)
