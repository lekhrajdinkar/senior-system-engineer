# 2. DFS : exercise (Binary Tree)

## ✔️Problem-1: Sum of Nodes
- `sum(node) = sum(node.left) + sum(node.right) + node.val`
-  bubbles up, from the leaf nodes up to the parent nodes until we reach the root node
-  each recursive call should return the **sum of its subtree**

@[code:section::DFS-return-problem-1](../../../../src/leetcode/hellointerview/DFS/exercise-1.py)

## ✔️Problem-2: Find the maximum value in a binary tree**
- `max(left, node.val, right )`

@[code:section::DFS-return-problem-2](../../../../src/leetcode/hellointerview/DFS/exercise-1.py)

---
## 104|E. Maximum Depth of Binary Tree
- https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
- https://www.hellointerview.com/learn/code/depth-first-search/maximum-depth-of-binary-tree | skip

@[code:section::section-104](../../../../src/leetcode/hellointerview/DFS/exercise-2.py)

---
## 112|E. Path Sum
- https://leetcode.com/problems/path-sum/description/
- https://www.hellointerview.com/learn/code/depth-first-search/path-sum | skip

@[code:section::section-112,section-112-hi](../../../../src/leetcode/hellointerview/DFS/exercise-2.py)

---
## 1448|M. Count Good Nodes in Binary Tree ⭐⭐
> Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.
- https://leetcode.com/problems/count-good-nodes-in-binary-tree/description/
- https://www.hellointerview.com/learn/code/depth-first-search/global-variables

@[code:section::section-1448](../../../../src/leetcode/hellointerview/DFS/exercise-2.py)

---
## 98|M. Validate Binary Search Tree 🔺
> - Every node in the left subtree of the root node, must have a value less than the value of the root node.
> - Every node in the right subtree of the root node, must have a value greater than the value of the root node.
- https://www.hellointerview.com/learn/code/depth-first-search/validate-binary-search-tree
- https://leetcode.com/problems/validate-binary-search-tree/description/

![img.png](../../../99_img/2026/07/02/02/img.png)
![img_1.png](../../../99_img/2026/07/02/02/img_1.png)

```visualize
             5
          (-∞, ∞)
           /     \
          4       6
      (-∞,5)    (5,∞)
```

@[code:section::section-98](../../../../src/leetcode/hellointerview/DFS/exercise-2.py)

---
## XXX. XXX

@[code:section::section-00](../../../../src/leetcode/hellointerview/DFS/exercise-2.py)

---
## XXX. XXX

@[code:section::section-00](../../../../src/leetcode/hellointerview/DFS/exercise-2.py)