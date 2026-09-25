# DFS:  on Binary Tree
## References
- [02_Binary-Tree.md](../../01_DS/02_Binary-Tree.md)
- https://leetcode.com/problem-list/depth-first-search/
- https://www.hellointerview.com/learn/code/depth-first-search/introduction
- https://www.hellointerview.com/learn/code/depth-first-search/fundamentals

---
## DFS: Overview
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

Time and Space Complexity
- there are `N` nodes in a binary tree
- `O(N)`
- `O(N)`

---
## DFS implementation :: on Binary Tree
### 1. Traversal 

[02_dfs-in-tree.excalidraw](../../draw/03/07_DFS/02_dfs-in-tree.excalidraw)

@[code:section:DFS-template-1](../../../../../src/leetcode/hellointerview/DFS/exercise-0.py)

> whenever a recursive function returns, we have finished visiting all nodes in the left and right subtrees of the current node

**Recursion and the Call Stack**
-  DFS is typically implemented as a recursive function
- call stack is a stack-like data structure that keeps track of the function calls that are currently being executed.
- When a **recursive** call is made, a new call frame is pushed onto the call stack.
- **Backtracking**
  - Backtracking occurs whenever a **recursive call returns**.
  - When the function returns, the call frame is popped off the call stack
  - and execution returns to the call frame that is now at the top of the call stack.
  - Backtracking (continued)
- This process continues until we have visited all the nodes in the binary tree.

---
### 2. Return Values
- the next step is to have each recursive call to DFS, **return a value**
- Make sure to return value of the **base case**

> ask yourself: What information do I need from my left and right subtrees to solve the problem for my subtree?
> - Find the maximum value in a binary tree
> - sum of nodes
> - ...

**✔️Problem-1: Sum of Nodes**
- `sum(node) = sum(node.left) + sum(node.right) + node.val`
-  bubbles up, from the leaf nodes up to the parent nodes until we reach the root node
-  each recursive call should return the **sum of its subtree**

**✔️Problem-2: Find the maximum value in a binary tree**
- `max(left, node.val, right )`

---
### 3. Pass Values
- in some cases, questions require us to **pass information down** from parents to child nodes
- If we need more parameters than the original function signature allows, then we need to introduce a **helper function** to help us

