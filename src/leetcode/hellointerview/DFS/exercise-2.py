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

# ============================================

class Solution:
    # section::section-3::start
    # Copy Graph - Build adjList from IntGraphNode
    def copy_graph(self, node: IntGraphNode) -> Dict[int, List[int]]:
        def dfs(node: IntGraphNode, visited):
            nonlocal adjList
            if node is None: return
            if node.value in visited: return

            adjList[node.value] = [ x.value for x in node.neighbors]
            visited.add(node.value)

            for x in node.neighbors: dfs(x, visited) # DFS into neighbors

        visited = set(); adjList = {}
        dfs(node, visited) # start here
        return adjList
    # section::section-3::end

    # ===============================================
    # section::section-util-1::start
    def build_adj_list(self, n:int, edges: List[List[int]]) -> dict:
        adj_list = {i: [] for i in range(n)}
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        print(f">> build_adj_list: {adj_list}")
        return adj_list
    # section::section-util-1::end

    # section::section-4::start
    # valid graph tree - no cycle, no disconnected node
    def graph_valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = self.build_adj_list(n, edges) # neighbours 👈
        visited = set()
        def hasCycle(node:int, parent:int) -> bool: # c
            #if node in visited: return False
            visited.add(node)
            for nbr in adjList[node]:
                # Ignore the edge we came from
                if nbr == parent: continue

                # Already visited through another path → cycle
                if nbr in visited: return True

                # DFS into neighbor
                if hasCycle(nbr, node): return True

            return False

        if hasCycle(0,-1): return False # Check cycle | condition 1
        return True if len(visited) == n else False # Check single connectivity | condition 2
    # section::section-4::end

# ===============

if __name__ == "__main__":

    def graph_valid_tree_text():
        Solution().graph_valid_tree(n=4, edges=[[0,1],[2,3]])
        Solution().graph_valid_tree(n=2, edges=[[0,1]])
        Solution().graph_valid_tree(n=5, edges=[[0,1],[0,2],[0,3],[1,3],[1,4]])
        Solution().graph_valid_tree(n=6, edges=[[0,1],[1,2],[2,0],[3,4],[4,5]])


    graph_valid_tree_text()