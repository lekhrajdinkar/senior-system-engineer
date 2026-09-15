# 3. DFS : exercise (Graph)

[graph-2d-matrices.excalidraw](../draw/03/07_DFS/01_problem-connected-island.excalidraw)

---
## problem-1: Counting Connected Components
@[code:section:section-1](../../../../src/leetcode/hellointerview/DFS/exercise-0.py)

---
## problem-2: Boundary
- same as counting problem, but from boundary
- find cells that are connected to the edge of a grid.  Meaning, all connected cells which are on boundary of the matrix.
    - "Surrounded Regions"
    - "Pacific Atlantic Water Flow.
- trick: start from the border and see which cells can be reached from this boundary cell.

@[code:section:section-2](../../../../src/leetcode/hellointerview/DFS/exercise-0.py)

---
## problem-3. Copy Graph
- Build `adjList` from `IntGraphNode`
- https://www.hellointerview.com/learn/code/depth-first-search/copy-graph

@[code:section::section-3,section-0](../../../../src/leetcode/hellointerview/DFS/exercise-2.py)

---
## problem-4. Graph Valid Tree
- https://www.hellointerview.com/learn/code/depth-first-search/graph-valid-tree
> valid graph tree - no cycle, no disconnected node

[05_valid-graph-as-tree.excalidraw](../draw/03/07_DFS/05_valid-graph-as-tree.excalidraw)



@[code:section::section-4](../../../../src/leetcode/hellointerview/DFS/exercise-2.py)
@[code:section::section-util-1](../../../../src/leetcode/hellointerview/DFS/exercise-2.py)