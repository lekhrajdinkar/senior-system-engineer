# 3. DFS : exercise (Graph)

## problem-1: Counting Connected Components
### tab:1 solution
@[code:section:section-1](../../../../src/leetcode/hellointerview/DFS/exercise-0.py)
### tab:2  visuals
[graph-2d-matrices.excalidraw](../draw/03/07_DFS/01_problem-connected-island.excalidraw)

---
## problem-2: Boundary
- same as counting problem, but from boundary
- find cells that are connected to the edge of a grid.  Meaning, all connected cells which are on boundary of the matrix.
    - "Surrounded Regions"
    - "Pacific Atlantic Water Flow.
- trick: start from the border and see which cells can be reached from this boundary cell.

### tab:1 solution
@[code:section:section-2](../../../../src/leetcode/hellointerview/DFS/exercise-0.py)
### tab:2  visuals
[graph-2d-matrices.excalidraw](../draw/03/07_DFS/01_problem-connected-island.excalidraw)

---
## problem-3. Copy Graph
- Build `adjList` from `IntGraphNode`
- https://www.hellointerview.com/learn/code/depth-first-search/copy-graph

@[code:section::section-3,section-0](../../../../src/leetcode/hellointerview/DFS/exercise-2.py)

---
## problem-4. Graph Valid Tree ⭐⭐
- https://www.hellointerview.com/learn/code/depth-first-search/graph-valid-tree
> valid graph tree - no cycle, no disconnected node

### tab:1 solution
@[code:section::section-4](../../../../src/leetcode/hellointerview/DFS/exercise-2.py)
@[code:section::section-util-1](../../../../src/leetcode/hellointerview/DFS/exercise-2.py)

### tab:2  visuals
[05_valid-graph-as-tree.excalidraw](../draw/03/07_DFS/05_valid-graph-as-tree.excalidraw)

---
## 733 | E. Flood Fill
- https://www.hellointerview.com/learn/code/depth-first-search/flood-fill
- https://leetcode.com/problems/flood-fill/description/

@[code:section::section-733](../../../../src/leetcode/hellointerview/DFS/exercise-2.py)

---
## 200 | M. number-of-islands
- https://www.hellointerview.com/learn/code/depth-first-search/number-of-islands
- https://leetcode.com/problems/number-of-islands/

@[code:section::section-733](../../../../src/leetcode/hellointerview/DFS/exercise-2.py)

---
## 130 | M. surrounded-regions
- https://www.hellointerview.com/learn/code/depth-first-search/surrounded-regions
- https://leetcode.com/problems/surrounded-regions/description/

@[code:section::section-130](../../../../src/leetcode/hellointerview/DFS/exercise-2.py)

---
## 417 | M. pacific-atlantic-water-flow
- https://www.hellointerview.com/learn/code/depth-first-search/pacific-atlantic-water-flow
- https://leetcode.com/problems/pacific-atlantic-water-flow/description/

@[code:section::section-417](../../../../src/leetcode/hellointerview/DFS/exercise-2.py)