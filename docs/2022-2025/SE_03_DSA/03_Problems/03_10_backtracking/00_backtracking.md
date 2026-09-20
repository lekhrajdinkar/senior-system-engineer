# Back tracking
## Reference
- [DFS_Theory :: binary_tree.md](../03_08_DFS/02_01_DFS_on_binary_tree.md)
- [DFS_Exercise :: Binary-Tree.md](../03_08_DFS/02_02_Exercise-Binary-Tree.md)
- https://www.hellointerview.com/learn/code/backtracking/overview

## overview
> back tracking = DFS + Decision/undo

- It finds a solution for the problem by **exploring all possible paths** like DFS
- **It "backtracks" to the previous path** as soon as the current path doesn't lead to a solution. this is **pruning**

---
## 113 | M. PathSum 2
- https://leetcode.com/problems/path-sum-ii/description/
- https://www.hellointerview.com/learn/code/depth-first-search/path-sum-2

**Summary**
- It explores all possible root-to-leaf paths in the binary tree to find the paths that sum to the target sum.
- Whenever we reach a leaf node, we backtrack to the previous node in the tree to explore the next path.
- It "prunes" paths by returning immediately when the sum exceeds the target sum.

### tab:1 Solution: BackT
@[code:section::problem-113](../../../../../src/leetcode/hellointerview/backtracking/exercise-1.py)

### tab:2 visual
[07_problems.excalidraw](../../draw/03/07_DFS/07_problems.excalidraw)

### tab:3 Solution: DFS
@[code:section::section-113](../../../../../src/leetcode/hellointerview/DFS/exercise-1.py)

