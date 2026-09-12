# 2. DFS:  on Binary Tree
## Overview
> Pattern:
> - finding depth,
> - validating structure,
> - and path problems

## Binary tree
- The **height** of a binary tree is the **number of edges** on the longest path between the root node and a leaf node
- A binary tree is **balanced** if the height of the left and right subtrees of every node differ by at most 1
- A binary tree is **complete** if every level, except possibly the last, is completely filled, and all nodes are as far left as possible.
- A **binary search tree (BST)** is a binary tree where:
  - All nodes in the left subtree of the root have a value less than the root.
  - All nodes in the right subtree of the root have a value greater than the root.

[03_bs.excalidraw](../draw/03/07_DFS/03_bs.excalidraw)

---
## Traversal on binary tree | DFS implementation
[02_dfs-in-tree.excalidraw](../draw/03/07_DFS/02_dfs-in-tree.excalidraw)

```python
def dfs(node): # DFS on binary tree
  if  node is None:
    return # prevent from going beyond leaf nodes

  # process the current node
  dfs(node.left)
  dfs(node.right)
```

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

> whenever a recursive function returns, we have finished visiting all nodes in the left and right subtrees of the current node

---
## Time and Space Complexity
- there are N nodes in a binary tree
- O(N).
- O(N)