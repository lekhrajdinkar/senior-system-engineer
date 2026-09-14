# 3. DSA: on Graph
## Overview
> Pattern: 
> - connected components
> - boundary traversal
> - cycle detection

```python
def dfs(node, visited):
    if node in visited:
        return
    
    visited.add(node)
    
    for neighbor in node.neighbors:
        dfs(neighbor, visited)
```
- Graph problems **add complexity**: 
  - you need to handle cycles, 
  - different representations (adjacency lists and matrices), 
  - and sometimes disconnected components.
- DFS on:
  - adjacency list representations
  - **2D matrix grids** (seen in below 2 problems)


---
## Exercise
[Exercise-2-Graph.md](03_Exercise-Graph.md)