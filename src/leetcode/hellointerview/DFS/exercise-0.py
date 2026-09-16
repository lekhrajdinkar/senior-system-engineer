# ============ DFS on graph : 2d matrix ====
from typing import List


# section::section-2::start
def find_boundary_connected(grid: List[List[int]]):
    rows, cols = len(grid), len(grid[0])
    visited = set()
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    def dfs(r, c):
        if (r, c) in visited: return
        if r < 0 or r >= rows or c < 0 or c >= cols: return
        if grid[r][c] != 1: return # break

        # grid[r][c] = 9 #  mark land with 9

        visited.add((r, c))
        for dr, dc in directions: # DFS on neighbours
            dfs(r + dr, c + dc)

    # Start DFS from boundary cells with value 1 ⭐
    for r in range(rows):
        if grid[r][0] == 1: dfs(r, 0) # col-0
        if grid[r][cols-1] == 1: dfs(r, cols-1) # col-last
    for c in range(cols):
        if grid[0][c] == 1: dfs(0, c) # row-0
        if grid[rows-1][c] == 1: dfs(rows-1, c) # row-last

    print(visited) # see answer, coordinates
# section::section-2::end


# ============ DFS on Binart tree  ====

# section::DFS-return-problem-1::start
def dfs(node):
    # base case: empty subtree
    if node is None:
        return 0

    # base case: leaf node
    if node.left is None and node.right is None:
        return node.val

    left = dfs(node.left)
    right = dfs(node.right)
    return left + node.val + right
# section::DFS-return-problem-1::end

# section::DFS-return-problem-2::start
def maxValue(node):
    # base case: empty subtree
    if node is None:
        # An empty subtree has a maximum value of negative infinity.
        return float('-inf')

    # base case: leaf node
    if node.left is None and node.right is None:
        return node.val

    left = maxValue(node.left)
    right = maxValue(node.right)
    return max(left, node.val, right ) # ⭐
# section::DFS-return-problem-2::end