# Back tracking
## Reference
- [DFS_Theory :: binary_tree.md](../03_08_DFS/02_01_DFS_on_binary_tree.md)
- [DFS_Exercise :: Binary-Tree.md](../03_08_DFS/02_02_Exercise-Binary-Tree.md)
- https://www.hellointerview.com/learn/code/backtracking/overview
- https://www.hellointerview.com/learn/code/backtracking/solution-space-trees

## overview
> back tracking = DFS + Decision/undo

- It finds a solution for the problem by **exploring all possible paths** like DFS
- **It "backtracks" to the previous path** as soon as the current path doesn't lead to a solution. this is **pruning**
- Backtracking on: 
  - Binary Tree (`# 113`)
  - Graph (`# 79`)
  - **Solution Space Trees**  ⭐

> In most backtracking problems, we won't be given an explicit tree to traverse. Instead, our algorithm needs to construct the tree based on the problem

## 00. letter combination 🟡
- solution space tree
- https://www.hellointerview.com/learn/code/backtracking/solution-space-trees

---
## 78. subsets 🟡
- Solution space Tree
- https://www.hellointerview.com/learn/code/backtracking/subsets
- https://leetcode.com/problems/subsets/description/

### tab:1 solution
@[code:section::problem-78](../../../../../src/leetcode/hellointerview/backtracking/exercise-1.py)

### tab:2 visual
[01_subset.excalidraw](../../draw/03/09_backT/01_subset.excalidraw)

---
## 22. generate-parentheses 🟡
- Solution space Tree
- https://www.hellointerview.com/learn/code/backtracking/generate-parentheses
- https://leetcode.com/problems/generate-parentheses/description/

**Rule/logic**
- starting from an empty string `s = ""`
- We can add an opening parenthesis `(` to s
  - if the number of opening parentheses in s < `n`.
- We can add a closing parenthesis `)` to s
  - if the number of closing parentheses in s < number of opening parentheses in s.

@[code:section::problem-22](../../../../../src/leetcode/hellointerview/backtracking/exercise-1.py)

---
## 39. combination-sum
- Solution space Tree
- https://www.hellointerview.com/learn/code/backtracking/combination-sum
- https://leetcode.com/problems/combination-sum/description/

Example
- Input: candidates = [2,3,5], target = 8
- Output: [[2,2,2,2],[2,3,3],[3,5]]

@[code:section::problem-39](../../../../../src/leetcode/hellointerview/backtracking/exercise-1.py)

---
## 131. palindrome-partitioning
- https://www.hellointerview.com/learn/code/backtracking/palindrome-partitioning
- https://leetcode.com/problems/palindrome-partitioning/description/

@[code:section::problem-131](../../../../../src/leetcode/hellointerview/backtracking/exercise-1.py)

---
## 51. n-queens
- https://leetcode.com/problems/n-queens/description/
- https://www.hellointerview.com/learn/code/backtracking/n-queens

@[code:section::problem-51](../../../../../src/leetcode/hellointerview/backtracking/exercise-1.py)

---
## 79.  word-search ⭐
- Graph (2d Matrix)
- https://leetcode.com/problems/word-search/description/
- https://www.hellointerview.com/learn/code/backtracking/word-search

@[code:section::problem-79-DFS-2,problem-79-DFS-1,problem-79-BACKT-1-hi](../../../../../src/leetcode/hellointerview/backtracking/exercise-1.py)

---
## 113 | M. PathSum 2 ✔️
- Binary Tree
- https://leetcode.com/problems/path-sum-ii/description/
- https://www.hellointerview.com/learn/code/depth-first-search/path-sum-2

**Summary**
- It explores all possible root-to-leaf paths in the binary tree to find the paths that sum to the target sum.
- Whenever we reach a leaf node, we backtrack to the previous node in the tree to explore the next path.
- It "prunes" paths by returning immediately when the sum exceeds the target sum.

### tab:1 Solution
@[code:section::problem-113](../../../../../src/leetcode/hellointerview/backtracking/exercise-1.py)

### tab:2 visual
[07_problems.excalidraw](../../draw/03/07_DFS/07_problems.excalidraw)

### tab:3 Solution: DFS
@[code:section::section-113](../../../../../src/leetcode/hellointerview/DFS/exercise-1.py)