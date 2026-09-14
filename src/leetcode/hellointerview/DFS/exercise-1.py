# ===== C. leetCode ========
import heapq
from typing import Optional, List
from src.leetcode.hellointerview.DFS.util import TreeNode, array_to_tree, draw_tree


class Solution:
    # section::section-104::start
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def dfs(depth: int, node): # gives depth
            if node is None:
                return 0
            elif node.left is None and node.right is None:
                print(f"depth from root at leaf-node {node.val} : {depth}")
                return depth
            else:
                print(f"depth from root at node {node.val} : {depth}")
                left   = dfs(depth+1, node.left)
                right  = dfs(depth+1, node.right)

                # capture max_depth ⭐
                max_depth = max(left, right)
                print(f"\nmax_depth : {max_depth}")
                return max_depth

        return dfs(1, root)
    """
    root = [3,9,20,null,null,15,7]
    
    depth at leaf node 9 : 2
    depth at leaf node 15 : 3
    depth at leaf node 7 : 3
    depth at node 20 : 3
    depth at node 3 : 3
    """
    # section::section-104::end

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
    # section::section-112::start
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # root-to-leaf paths 👈
        def sumToPath( node:TreeNode, partialSum: int) -> bool:
            if node is None:
                return False
            if node.left is None and node.right is None:
                print(f"leaf node : {node.val} , sum till leaf : {partialSum + node.val}")
                return True if partialSum + node.val == targetSum else False
            else:
                partialSum = partialSum + node.val
                print(f"node : {node.val} , new partialSum : {partialSum}")
                if sumToPath(node.left,partialSum): return True
                else: return sumToPath(node.right,partialSum)
                # return sumToPath(node.left,partialSum, targetSum) or sumToPath(node.right,partialSum, targetSum)
        return sumToPath(root, 0)
    # section::section-112::end

    # section::section-113::start
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        # root-to-leaf paths  👈
        def sumToPath( node:TreeNode, partialSum: int, arr: List[int]) :
            nonlocal result

            if node is None:
                return
            elif node.left is None and node.right is None:
                arr.append(node.val); partialSum = partialSum + node.val
                print(f"node : {node.val} , new partialSum : {partialSum}, arr: {arr} | Leaf")

                if partialSum == targetSum:
                    print(f"\tmatching root2leaf_pathSum: {partialSum} with targetSum: {targetSum}")
                    result.append(arr[:])
                    print(f"\tresult: {result}")

            else:
                arr.append(node.val); partialSum = partialSum + node.val
                print(f"node : {node.val} , new partialSum : {partialSum}, arr: {arr}")

                sumToPath(node.left, partialSum, arr) # sumToPath(node.left, partialSum, arr[:])
                sumToPath(node.right, partialSum, arr) # sumToPath(node.right, partialSum, arr[:)

            arr.pop() # backtracking ⭐

        result = []
        sumToPath(root, 0, [])
        return result
    # section::section-113::end


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

    # section::section-563::start
    def findTilt(self, root: Optional[TreeNode]) -> int:
        def dfs_sum(node: TreeNode):
            nonlocal tiltSum
            if node is None:
                return 0
            elif node.left is None and node.right is None:
                return node.val # just return Sum
                # leaf Node has 0 tilt, so ignore
            else:
                left = dfs_sum(node.left)
                right = dfs_sum(node.right)
                # tilt sum ⭐
                tiltSum = tiltSum +  abs(right - left)
                if node.val: print(f"node: {node.val}, left: {left}, right:{right}, tilt: {abs(right - left)} | tiltSum: {tiltSum}")
                return left + node.val + right

        tiltSum = 0
        dfs_sum(root)
        return tiltSum
    # section::section-563::end

    # section::section-543::start
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node:TreeNode): # gives depth
            nonlocal max_diameter
            if node is None: # Height of empty subtree
                return 0
            else:
                left   = dfs(node.left)
                right  = dfs(node.right)

                # capture diameter
                max_diameter = max(max_diameter, (left + right))
                print(f"Node: {node.val} | Left height: {left} | Right height: {right} | Diameter: {(left + right)} | Max: {max_diameter}")
                # return depth from parent node (Not ROOT)
                return 1 + max(left, right) # Return height to parent 👈👈⭐

        max_diameter = 0
        dfs(root)
        return max_diameter
    # section::section-543::end

    # section::section-687::start
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        # dfs(node,depth) returns the longest downward path
        # starting from node where all values are equal to node.val.
        def dfs_depth( node :TreeNode, depth) -> int:
            nonlocal result
            if node is None:
                return 0
            elif node.left is None and node.right is None:
                print(f"Leaf Node: {node.val}(depth:{depth})")
                return depth
            else:
                l = 0; r = 0
                print(f"Node: {node.val}(depth:{depth})")

                if node.left and node.left.val == node.val:
                    l = dfs_depth(node.left, depth+1)
                else:
                    l = dfs_depth(node.left, 0)

                if node.right and node.right.val == node.val:
                    r = dfs_depth(node.right, depth+1)
                else:
                    r = dfs_depth(node.right, 0)

                result = max( result, l+r)
                print(f"Node: {node.val}(depth:{depth}) | Left: {l} | Right: {r} | Result: {l+r} | max_ : {result}")
                return max(l,r) # Return longest ONE direction to parent

        result = 0
        dfs_depth(root,0)
        return result

        """
        │       ┌── 5
        │   ┌── 5
        └── 5
            │   ┌── 1
            └── 4
                └── 1
        Node: 5(depth:0)
        Node: 4(depth:0)
        Leaf Node: 1
        Leaf Node: 1
        Node: 4(depth:0) | Left: 0 | Right: 0 | Result: 0 | max_ : 0
        Node: 5(depth:1)
        Leaf Node: 5
        Node: 5(depth:1) | Left: 0 | Right: 2 | Result: 2 | max_ : 2
        Node: 5(depth:0) | Left: 0 | Right: 2 | Result: 2 | max_ : 2
        """
    # section::section-687::end

# =============main======

if __name__ == "__main__":

    def test_113(): # 113: pathSum
        arr1 = [1,2,4,4,7,5,1]
        arr2 = [5,4,8,11,None,13,4,7,2,None,None,5,1]
        print('='*50);Solution().pathSum(array_to_tree(arr2), 22)
        print('='*50);Solution().pathSum(array_to_tree(arr1), 22)

    def test_687(): # 687: longestUnivaluePath
        print('='*50);Solution().longestUnivaluePath(array_to_tree([1,4,5,4,4,None,5]))
        print('='*50);Solution().longestUnivaluePath(array_to_tree([5,4,5,1,1,None,5]))
        print('='*50);Solution().longestUnivaluePath(array_to_tree([1,2,2,2,2]))
        print('='*50);Solution().longestUnivaluePath(array_to_tree([1,None,1,1,1,1,1,1]))


    #test_113()
    test_687()