# DSA: Depth-First Search
## Reference
- https://www.hellointerview.com/learn/code/depth-first-search/introduction

## Overview
> Understanding when to use DFS vs BFS is critical.
> - In short: use DFS when you need to explore all paths or find any valid solution,
> - use BFS when you need the shortest path or level-by-level traversal.

- DFS arguably the **most important algorithm** to master for coding interviews.
- It's called "depth-first" because 
  - it explores **as far down a path as possible** before backtracking to try another path
  - go deep, then backtrack
- DFS is a **traversal algorithm** for:
    - **trees** : 
      - have no cycles, so don't need to track visited nodes
      - We start with DFS on **binary trees** because they're the simplest structure to work
    - **graphs**: 
      - have cycle
  
---
## 1. Tree
> Pattern: 
> - finding depth, 
> - validating structure, 
> - and path problems

```tree
dfs(node):
  if node is null
    return

  // process the current node

  dfs(node.left)
  dfs(node.right)
```

---
## 2. Graph
> Pattern: 
> - connected components, 
> - boundary traversal, 
> - cycle detection


```graph
dfs(node, visited)
    if node in visited
        return
    
    visited.add(node)
    
    for neighbor in node.neighbors
        dfs(neighbor, visited)
```
- Graph problems add complexity: 
  - you need to handle cycles, 
  - different representations (adjacency lists and matrices), 
  - and sometimes disconnected components.
- DFS on 
  - adjacency list representations
  - 2D matrix grids

---

## problem-1: Counting Connected Components

[01_problem-connected-island.excalidraw](../draw/03/07_DFS/01_problem-connected-island.excalidraw)

@[code:section:section-1](../../../../src/leetcode/hellointerview/DFS/exercise-1.py)
@[code:section:section-0](../../../../src/leetcode/hellointerview/DFS/exercise-1.py)

## problem-2: Boundary
- same as counting problem, but from boundary
- find cells that are connected to the edge of a grid.  Meaning, all connected cells which are on boundary of the matrix.
  - "Surrounded Regions" and "Pacific Atlantic Water Flow.
- trick: start from the border and see which cells can be reached from this boundary cell.

@[code:section:section-2](../../../../src/leetcode/hellointerview/DFS/exercise-1.py)

## Conclusion
DFS excels when you need to:
- Explore **all possible paths** (like finding all solutions or any valid solution)
- **Traverse hierarchical structures** (trees, nested data)
- Find connected components in graphs or grids
- **Detect cycles in graphs**
- Process nodes in a specific order (pre-order, in-order, post-order)

> Note: If you need the **shortest path** in an unweighted graph, use `BFS` instead. DFS finds a path, not necessarily the shortest one.