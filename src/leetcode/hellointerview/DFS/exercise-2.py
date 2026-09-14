# ===== C. leetCode ========
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


    # ==========================
    # section::section-1448::start
    def goodNodes(self, root:  Optional[TreeNode]) -> int:
        def dfs2(node: TreeNode, parentValue: int) -> int :
            count=0
            # dont need to handle leaf case
            if node is None:
                return 0
            else:
                if node.val >= parentValue:count+=1
                l = dfs2(node.left, node.val)
                r = dfs2(node.right, node.val)
                return l + count + r

        # same as dfs2() function above, but does not return
        count = 0
        def dfs(node: TreeNode, parentValue: int) :
            nonlocal count # 👈👈
            if node is None:
                pass
            elif node.left is None and node.right is None:
                if node.val >= parentValue:
                    count+=1
                    print(f"leaf Node: {node.val} > parent Node : {parentValue} | count: {count}" )
                #else: print(f"leaf Node: {node.val} < parent Node : {parentValue} 🔺"  )
            else:
                if node.val >= parentValue:
                    count+=1
                    print(f"Node: {node.val} > parent Node : {parentValue} | count: {count}" )
                #else: print(f"Node: {node.val} < parent Node : {parentValue} 🔺"  )

                dfs(node.left, node.val)
                dfs(node.right, node.val)

        #dfs(root,root.val);print(f"Final good node count: {count}")
        count=dfs2(root,root.val); print(f"Final good node count: {count}")
        return count  # assumes root is non-null
    # section::section-1448::end


    # ==========================
    # section::section-98::start
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, lower, upper):
            if node is None:
                return True

            print( f"Node: {node.val} | " f"Valid Range: ({lower}, {upper})")
            if not (lower < node.val < upper):
                print(f"🔺 Node {node.val} is outside range ({lower}, {upper})")
                return False

            print(f"✅ Node {node.val} is valid")

            # this logic is by ChapGPT ⭐
            left = dfs(node.left, lower, node.val)
            right = dfs(node.right, node.val, upper)

            return left and right
        return dfs(root, float("-inf"), float("inf"))
    # section::section-98::end

    # ==========================
    # section::section-00::start
    def dfs(node: TreeNode):
        if node is None:
            return False
        elif node.left is None and node.right is None:
            pass
        else:
            pass
    # section::section-00::end
