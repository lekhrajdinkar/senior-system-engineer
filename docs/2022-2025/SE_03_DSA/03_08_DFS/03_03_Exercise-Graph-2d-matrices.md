#  DFS : exercise (Graph: 2D matrices)

---
## Visual
[graph_2d-matrices.excalidraw](../draw/03/07_DFS/06_graph_2d-matrices.excalidraw)

---
## Island count
### 200 | M. number-of-islands (All)
- https://www.hellointerview.com/learn/code/depth-first-search/number-of-islands
- https://leetcode.com/problems/number-of-islands/

@[code:section:section-200](../../../../src/leetcode/hellointerview/DFS/exercise-3.py)

### From Boundary
- same as counting problem, but from boundary
- find cells that are connected to the edge of a grid.  Meaning, all connected cells which are on boundary of the matrix.
    - "Surrounded Regions"
    - "Pacific Atlantic Water Flow.
- trick: start from the border and see which cells can be reached from this boundary cell.

@[code:section:section-130-hint](../../../../src/leetcode/hellointerview/DFS/exercise-3.py)

---
## 733 | E. Flood Fill ✔️
- https://www.hellointerview.com/learn/code/depth-first-search/flood-fill
- https://leetcode.com/problems/flood-fill/description/

@[code:section::section-733-v2](../../../../src/leetcode/hellointerview/DFS/exercise-3.py)

---
## 130 | M. surrounded-regions
>   - find 0's cell from border - mark then S safe ⭐⭐
>   - for rest 0, flip to X and flip S back to 0

- https://www.hellointerview.com/learn/code/depth-first-search/surrounded-regions
- https://leetcode.com/problems/surrounded-regions/description/

@[code:section::section-130,section-130-hint](../../../../src/leetcode/hellointerview/DFS/exercise-3.py)

---
## 417 | M. pacific-atlantic-water-flow
- https://www.hellointerview.com/learn/code/depth-first-search/pacific-atlantic-water-flow
- https://leetcode.com/problems/pacific-atlantic-water-flow/description/

@[code:section::section-417](../../../../src/leetcode/hellointerview/DFS/exercise-3.py)