from typing import Dict, List

class Solution:
    # section::section-template-1::start
    def section(self, matrics: List[List[int]]):
        visited = set() # tuple (x,y) coordinate
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def dfs_helper(r, c):
            if (r, c) in visited: return
            if (r < 0 or r >= len(matrics))   or   (c < 0 or c >= len(matrics[0])): return
            visited.add((r, c))
            for dr, dc in directions: dfs_helper(r + dr, c + dc)  # DFS on neighbour
    # section::section-template-1::end

    # section::section-733-v2::start
    # Flood-fill ✔️
    def floodfill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        visited = set() # tuple (x,y) coordinate
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        parentOriginalColor = image[sr][sc]
        print(f"✔️--  fill color: {parentOriginalColor} with color: {color} --")

        def dfs_helper(r, c, depth): # DEPTH IS UNnecessary, added for print
            if (r, c) in visited: return
            if (r < 0 or r >= len(image))   or   (c < 0 or c >= len(image[0])): return
            visited.add((r, c))
            print(f"|{'__'*depth}🐛visited ({r},{c}), at depth {depth}")

            # here
            if image[r][c] == parentOriginalColor:
                print(f"|__{'__'*depth}Filled from color: {image[r][c]} to {color}")
                image[r][c] = color
            else: return # break was missing ⭐

            for dr, dc in directions: # DFS on neighbour run max 4 times
                dfs_helper(r + dr, c + dc, depth+1)

        dfs_helper(sr, sc, 1)
        """ 
        for r in range(sr, len(image)): # start point in not 0, check :)
            for c in range( sc, len(image[0])):
                if (r,c) not in visited:
                    dfs_helper(sr, sc, 1) # start from given point
        """
        return image
    # section::section-733-v2::end

    # section::section-200::start
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        count = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def dfs(r, c):
            if (r, c) in visited:return
            if r < 0 or r >= rows or c < 0 or c >= cols: return

            if grid[r][c] != "1": return # BREAK (if found non-connected)

            visited.add((r, c))
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        # each for each cell ⭐
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited: # ⭐
                    dfs(r, c) # ripple effect will get all connected nodes
                    count += 1 # once broke count all as single rock

        print(f"count: {count}")
        return count
    # section::section-200::end

    # section::section-130-hint::start
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
    # section::section-130-hint::end

    # section::section-130::start
    # find 0 cell from border - mark then S safe ⭐⭐
    # for rest 0, flip to X and flip S to 0
    def surrounded_regions(self, grid: List[List[str]]) -> List[List[str]]:
        # find 0 cell from border - mark then S safe ⭐⭐
        # for rest 0, flip to X and flip S to 0
        if not grid: return grid # special case

        rows, cols = len(grid), len(grid[0])
        visited = set()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(r, c):
            if (r, c) in visited: return
            if r < 0 or r >= rows or c < 0 or c >= cols: return
            if grid[r][c] != "O": return

            grid[r][c] = 'S' # ⭐STEP-1 mark boundary 0's SAFE (S)

            visited.add((r, c))
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for r in range(rows):
            if grid[r][0] == "O": dfs(r, 0) # col-0
            if grid[r][cols-1] == "O": dfs(r, cols-1) # col-last
        for c in range(cols):
            if grid[0][c] == "O": dfs(0, c) # row-0
            if grid[rows-1][c] == "O": dfs(rows-1, c) # row-last

        # ⭐ STEP-2 SWAP
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 'O': grid[i][j] = 'X'
                elif grid[i][j] == 'S': grid[i][j] = 'O'

        for rows in grid: print(rows) #  print result
        return grid
    # section::section-130::end

    # section::section-417::start
    # section::section-417::end


# ===============

if __name__ == "__main__":
    def floodfill_test():
        print('»'*30);Solution().floodfill([[1, 0, 1], [1, 0, 0], [0, 0, 1]], 2, 1, 2)
        print('»'*30);Solution().floodfill([[2, 2, 2], [2, 2, 0], [2, 0, 1]], 1, 1, 3)
        print('»'*30);Solution().floodfill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 2, 2, 2)

    def numIslands_test(): # 200
        print('»'*30);Solution().numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]])
        print('»'*30);Solution().numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]])

    #floodfill_test()
    numIslands_test()

    print('»'*30);Solution().surrounded_regions([["O","X","X","X"],["X","O","O","X"],["X","O","O","X"],["X",'X',"X","X"]])
    print('»'*30);Solution().surrounded_regions([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]])