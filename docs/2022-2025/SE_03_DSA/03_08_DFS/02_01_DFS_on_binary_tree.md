# DFS:  on Binary Tree
## Overview
> Pattern:
> - finding depth,
> - validating structure,
> - and path problems

---
## Time and Space Complexity
- there are `N` nodes in a binary tree
- `O(N)`
- `O(N)`

---
## Binary tree
> https://leetcode.com/problem-list/binary-tree/
- The **height** of a binary tree is the **number of edges** on the longest path between the root node and a leaf node
- A binary tree is **balanced** if the height of the left and right subtrees of every node differ by at most 1
- A binary tree is **complete** if every level, except possibly the last, is completely filled, and all nodes are as far left as possible.
- A **binary search tree (BST)** is a binary tree where:
  - All nodes in the left subtree of the root have a value less than the root.
  - All nodes in the right subtree of the root have a value greater than the root.

[03_bs.excalidraw](../draw/03/07_DFS/03_bs.excalidraw)

---
## DFS implementation (on binary tree)
### 1. Traversal 

[02_dfs-in-tree.excalidraw](../draw/03/07_DFS/02_dfs-in-tree.excalidraw)

```python
def dfs(node): # DFS on binary tree
  if  node is None:
    return # prevent from going beyond leaf nodes

  # process the current node
  dfs(node.left)
  dfs(node.right)
```
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

---
## More Exercises
[Exercise-1-BS.md](02_02_Exercise-BT.md)
