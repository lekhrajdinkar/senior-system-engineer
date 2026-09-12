# section::section-0::start

"""
[0, 1, 0, 0, 0, 0]
[0, 1, 1, 0, 1, 0]
[0, 0, 0, 1, 1, 0]
[1, 1, 0, 0, 0, 1]
[1, 1, 0, 0, 0, 1]
"""
# section::section-0::end

# section::section-1::start
def count_islands(grid):
    rows, cols = len(grid), len(grid[0])
    visited = set()
    count = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    def dfs(r, c):
        if (r, c) in visited:
            return
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return
        if grid[r][c] != 1:
            return
        visited.add((r, c))
        for dr, dc in directions:
            dfs(r + dr, c + dc)
    # each for each cell ⭐
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and (r, c) not in visited:
                dfs(r, c)
                count += 1
    return count
# section::section-1::end

# section::section-2::start
def find_boundary_connected(grid):
    rows, cols = len(grid), len(grid[0])
    visited = set()
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    def dfs(r, c):
        if (r, c) in visited:
            return
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return
        if grid[r][c] != 1:
            return
        visited.add((r, c))
        for dr, dc in directions:
            dfs(r + dr, c + dc)
    # Start DFS from boundary cells with value 1 ⭐
    for r in range(rows):
        if grid[r][0] == 1: dfs(r, 0)
        if grid[r][cols-1] == 1: dfs(r, cols-1)
    for c in range(cols):
        if grid[0][c] == 1: dfs(0, c)
        if grid[rows-1][c] == 1: dfs(rows-1, c)
# section::section-2::end
