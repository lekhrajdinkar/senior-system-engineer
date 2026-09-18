from collections import deque
from typing import Optional, List
from src.leetcode.hellointerview.BFS.util import array_to_tree


# section:TreeNode-class:start
class TreeNode:
    def __init__(self, vastart: int, left= None, right= None):
        self.val = val
        self.left = left
        self.right = right
# section:TreeNode-class:end

class Solution:
    # section:problem-1:start
    def level_order_sum(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        result: List[int] = []
        queue = deque([root]) # Queue of treeNode

        while queue:
            current_level_sum = 0

            level_size = len(queue)
            for _ in range(level_size):
                curend: TreeNode = queue.popleft()
                current_level_sum += curr.val # process
                if curr.left:  queue.append(curr.left)
                if curr.right: queue.append(curr.right)

            result.append(current_level_sum)

        return result
    # section:problem-1:end

    # section:problem-199:start
    # leetcode 199 | M
    def problem199(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        result: List[int] = []
        queue = deque([root]) # Queue of treeNode
        while queue:
            level_size = len(queue); curr = 0
            for _ in range(level_size):
                curr = queue.popleft()
                if curr.left:  queue.append(curr.left)
                if curr.right: queue.append(curr.right)
            if level_size > 0: result.append(curr.val)
        return result
    # section:problem-199:end

    # section:problem-103:start
    # 103. Binary Tree Zigzag Level Order Traversal
    def problem103(self, root: Optional[TreeNode]):
        if not root: return []
        result:list[list[int]] = []
        queue = deque([root]) # Queue of treeNode
        level = 0
        while queue:
            # adding a for-loop that iterates over, the size of the queue, at the beginning of each level
            level_size = len(queue); level +=1
            level_result = []
            for _ in range(level_size):
                curend: TreeNode = queue.popleft()

                # process here 1 ⭐
                level_result.append(curr.val)

                if curr.left:  queue.append(curr.left)
                if curr.right: queue.append(curr.right)

            # 💡 finished processing all nodes at the current level
            # process here 2 ⭐
            # could use another dequeue to append from both end. slicing would eat more space. 👈
            result.append(level_result if level%2 == 0 else level_result[::-1])
        print("problem103: ", result)
        return result

    """
        │       ┌── 7
    │   ┌── 20
    │   │   └── 15
    └── 3
        └── 9
    problem103:  [[3], [9, 20], [7, 15]]
    """
    # section:problem-103:end

    # section:problem-662:start
    # 662. Maximum Width of Binary Tree
    def problem662(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        queue = deque([(root, 0)])  # (node, position)
        max_width = 1
        while queue:
            level_size = len(queue)
            # level start
            first = queue[0][1] # first item
            last = first

            for _ in range(level_size):
                node, pos = queue.popleft() # pop first ite, then 2nd and till last
                last = pos # eventually will have last item position
                if node.left:  queue.append((node.left, 2 * pos + 1))
                if node.right: queue.append((node.right, 2 * pos + 2))

            width = last - first + 1
            max_width = max(max_width, width)

        return max_width
    # section:problem-662:end


    # ======================================================
    # section:problem-00:start
    def problem00(self, root: Optional[TreeNode]):
        if not root: return []
        queue = deque([root]) # Queue of treeNode
        while queue:
            # == level start here ==
            level_size = len(queue)
            # adding a for-loop that iterates over, the size of the queue, at the beginning of each level
            for _ in range(level_size):
                curr = queue.popleft()
                # process here 1 ⭐
                if curr.left:  queue.append(curr.left)
                if curr.right: queue.append(curr.right)

            # 💡 finished processing all nodes at the current level
            # process here 2 ⭐
            # == level End here ==
    # section:problem-00:end


if __name__ == "__main__":
    #print('='*20);Solution().problem103(array_to_tree([3,9,20,None,None,15,7]))

    print('='*20);Solution().problem662(array_to_tree([1,3,2,5,3,None,9]))
    print('='*20);Solution().problem662(array_to_tree([1,3,2,5,None,None,9,6,None,7]))
    #print('='*20);Solution().problem662(array_to_tree([1,3,2,5]))