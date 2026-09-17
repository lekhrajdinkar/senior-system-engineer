# BFS : Tree
## Reference
- [02_Binary-Tree.md](../../01_DS/02_Binary-Tree.md)
- https://www.hellointerview.com/learn/code/breadth-first-search/introduction
- https://www.hellointerview.com/learn/code/breadth-first-search/fundamentals

---
## Overview
[01_basic.excalidraw](../../draw/03/08_BFS/01_basic.excalidraw)
- `O(n)` - space and time
- BFS is a **level-by-level** traversal algorithm
- visits all nodes **at the current level** before moving to the next level of the tree
- BFS uses a **queue** to keep track of the nodes it needs to visit
  - Add **root** it to the queue.
  - **remove** the node at the front of the queue + visit/process it
  - Add the **children** of the node to the back queue.
  - **Repeat**, until queue is not empty 
  - > py: from collections import deque

---
##  BFS :: binary tree
###  tab:2 Basic 

```python
from collections import deque
def bfs(root):
    if not root:  return []
    # 💡BFS uses a "queue" to keep track of the nodes it needs to visit.
    queue = deque([root]) 
   
    while queue: # 💡4. repeat
        curr_node = queue.popleft() # 💡 1. remove the node
        print(curr_node.val) # 💡2. process node         
        # 💡 3. Add the children
        if curr_node.left: queue.append(curr_node.left)
        if curr_node.right: queue.append(curr_node.right)
        
```

###  tab:1  Extended
> Using a **for-loop to iterate over the nodes at each level** is such a common pattern, that it is the version of BFS on binary trees you need to know for interviews.

```python
from collections import deque
def level_order(root: TreeNode):
    if not root: return []
    result = []
    queue = deque([root]) # Queue of treeNode
    
    while queue: # repeat
        current_level_result = [] # current level result

        # 💡adding a for-loop that iterates over,
        # the size of the queue, at the beginning of each level
        level_size = len(queue)
        for _ in range(level_size):
            curr = queue.popleft()
            current_level_result.append(curr.val) # process
            if curr.left: queue.append(curr.left)
            if curr.right: queue.append(curr.right)
        
        # 💡 IMPORTANT
        # we have finished processing all nodes at the current level
        result.append(current_level_result)
        
    return result
```

