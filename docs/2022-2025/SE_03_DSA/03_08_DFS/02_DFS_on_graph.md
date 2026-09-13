# 1. DSA: on Graph
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
## problems

[01_problem-connected-island.excalidraw](../draw/03/07_DFS/01_problem-connected-island.excalidraw)

### tab:1 problem-1: Counting Connected Components

@[code:section:section-1](../../../../src/leetcode/hellointerview/DFS/exercise-1.py)

### tab:2 problem-2: Boundary
- same as counting problem, but from boundary
- find cells that are connected to the edge of a grid.  Meaning, all connected cells which are on boundary of the matrix.
  - "Surrounded Regions" 
  - "Pacific Atlantic Water Flow.
- trick: start from the border and see which cells can be reached from this boundary cell.

@[code:section:section-2](../../../../src/leetcode/hellointerview/DFS/exercise-1.py)