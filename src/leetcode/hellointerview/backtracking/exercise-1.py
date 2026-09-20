# section:TreeNode-class:start
from src.leetcode.hellointerview.DFS.util import array_to_tree


class TreeNode:
    def __init__(self, val: int, left= None, right= None):
        self.val = val
        self.left = left
        self.right = right
# section:TreeNode-class:end

class Solution:
    # section:problem-113:start
    def pathSum(self, root, target):
        def backtrack(node, path, total):
            if not node: return

            path.append(node.val)
            total += node.val
            print(f"\nnode: {node.val}, target: {target}, path: {path} | total: {total}")

            # KEY STEP 2 ⭐⭐⭐ PRUNING
            # current sum exceeds target
            # so pop to remove the current node from the path
            # return to backtrack to previous node on the call stack
            if total > target:
                item = path.pop()
                print(f"- pop early ({item}), path: {path}")
                return

            if not node.left and not node.right:
                # add the path to the result
                # note we have to make a copy (path[:]) of the path
                # since future recursive calls modify path
                print(f"- reached leafNode, path: {path}")
                if total == target:
                    result.append(path[:])
                    print(f"- 💡result: {result}")
            else:
                backtrack(node.left, path, total)
                backtrack(node.right, path, total)

            # KEY STEP 1
            # Since we use a single list to store the current path across all recursive calls,
            # before returning, we have to pop the current node from that path to backtrack.
            item = path.pop()
            print(f"- pop ({item}), path: {path}")

        result = []
        backtrack(root, [], 0)
        return result
    # section:problem-113:end

# ---------------------------
if __name__ == "__main__":
    Solution().pathSum(array_to_tree([5,4,8,11,None,13,4,7,2,None,None,5,1]), 22)