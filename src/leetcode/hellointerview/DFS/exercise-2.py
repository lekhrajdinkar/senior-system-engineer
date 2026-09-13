import heapq
from typing import Optional

# section::section-0::start
class TreeNode:
     def __init__(self, val: int, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
         self.val = val
         self.left = left
         self.right = right
# section::section-0::end

class Solution:
    # section::section-104::start
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def depth(curr_level: int, node):
            if node is None:
                return 0
            if node.left is None and node.right is None:
                #print(f"current level : {curr_level}, node : {node.val}")
                return curr_level
            else:
                #print(f"current level : {curr_level}, node : {node.val}")
                level_left = depth(curr_level+1, node.left)
                level_right  = depth(curr_level+1, node.right)
                return max(level_left, curr_level, level_right)

        return depth (0, root)
    """
    root = [3,9,20,null,null,15,7]
    
    current level : 1, node : 3
    current level : 2, node : 9
    current level : 2, node : 20
    current level : 3, node : 15
    current level : 3, node : 7
    """
    # section::section-104::end

    # ==========================
    # section::section-112::start
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def sumToPath( node:TreeNode, partialSum: int, targetSum: int) -> bool:
            if node is None:
                return False
            if node.left is None and node.right is None:
                print(f"leaf node : {node.val} , sum till leaf : {partialSum + node.val}")
                if partialSum + node.val == targetSum:
                    return True
                else:
                    return False
            else:
                partialSum = partialSum + node.val
                print(f"node : {node.val} , new partialSum : {partialSum}")
                if sumToPath(node.left,partialSum, targetSum):
                    return True
                else:
                    return sumToPath(node.right,partialSum, targetSum)
                # return sumToPath(node.left,partialSum, targetSum) or sumToPath(node.right,partialSum, targetSum)


        return sumToPath(root, 0, targetSum)

    # section::section-112::end

    # ==========================
    # section::section-112-hi::start
    def pathSum_hi_sol(self, root, target):
        if root is None:
            return False

        # If we reach a leaf node, check if the target is equal to the leaf node's value
        if not root.left and not root.right:
            return target == root.val

        target -= root.val
        return self.pathSum_hi_sol(root.left, target) or self.pathSum_hi_sol(root.right, target)
    # section::section-112-hi::end
