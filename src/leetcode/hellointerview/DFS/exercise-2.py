# ===== D. leetCode (Graph) ========
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
    def dfs1(self, root: Optional[TreeNode]) -> int:
        pass
    # section::section-104::end

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
