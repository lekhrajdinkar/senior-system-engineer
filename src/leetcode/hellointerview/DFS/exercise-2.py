# ===== D. leetCode (Graph) ========
from typing import Optional
from typing import Dict, List

# section::section-TreeNode::start
class TreeNode:
     def __init__(self, val: int, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
         self.val = val
         self.left = left
         self.right = right
# section::section-TreeNode::end

# section::section-0::start
class IntGraphNode:
     def __init__(self, value, neighbors):
         self.value = value
         self.neighbors = neighbors
# section::section-0::end

# section::section-3::start
# Copy Graph
class Solution:
    def copy_graph(self, node: IntGraphNode) -> Dict[int, List[int]]:

        def dfs(node: IntGraphNode, visited):
            nonlocal adjList
            if node is None: return
            if node.value in visited: return

            adjList[node.value] = [ x.value for x in node.neighbors]
            visited.add(node.value)

            for x in node.neighbors: dfs(x, visited)

        visited = set()
        #adjList: Dict[int, List[int] = {}
        adjList = {}
        dfs(node, visited)

        return adjList
# section::section-3::end