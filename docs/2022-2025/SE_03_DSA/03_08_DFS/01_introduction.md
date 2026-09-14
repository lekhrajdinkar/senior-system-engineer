# DSA: DFS - Introduction
## Reference
- https://www.hellointerview.com/learn/code/depth-first-search/introduction
- https://www.hellointerview.com/learn/code/depth-first-search/fundamentals
- https://leetcode.com/problem-list/depth-first-search/

## Overview
> Understanding when to use DFS vs BFS is critical.
> - In short: use DFS when you need to explore all paths or find any valid solution,
> - use BFS when you need the shortest path or level-by-level traversal.

- DFS arguably the **most important algorithm** to master for coding interviews.
- It's called "depth-first" (go deep, then backtrack) because:
  - it explores **as far down a path as possible** before backtracking to try another path
  - achieve by **recursion**. **callStack** handles backtrack 👈👈
- DFS is a **traversal algorithm** for:
    - **trees** : 
      - have no cycles, so don't need to track visited nodes
      - We start with DFS on **binary trees** because they're the simplest structure to work
    - **graphs**: 
      - have cycle

---
## Conclusion
DFS excels when you need to:
- Explore **all possible paths** (like finding all solutions or any valid solution)
- **Traverse hierarchical structures** (trees, nested data)
- Find connected components in graphs or grids
- **Detect cycles in graphs**
- Process nodes in a specific order (pre-order, in-order, post-order)

---
Note: 
- If you need the **shortest path** in an unweighted graph, use `BFS` instead. DFS finds a path, not necessarily the shortest one.
- Breadth-First Search (BFS), which explores all the nodes at a "level" before moving on to the next level

