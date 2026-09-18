from collections import deque
from typing import List


class Solution:
    # section:problem-1-statement:start
    """
    You are given a chessboard of infinite size where the coordinates of
    each cell are defined by integer pairs (x, y).The knight piece moves
    in an L-shape, either two squares horizontally and one square vertically,
    or two squares vertically and one square horizontally.

    Write a function to determine the minimum number of moves required for the knight
    to move from the starting position (0, 0) to the target position (x, y).
    Assume that it is always possible to reach the target position, and
    that x and y are both integers in the range [-200, 200]
    """
    # section:problem-1-statement:end

    # section:problem-1:start
    def minimumKnightMoves(self, x: int, y: int) -> int:
        # rows, cols = len(matrix), len(matrix[0]) # infinite grid
        directions = [ # ⭐
            (2, -1), (2, 1), (-2, -1), (-2, 1),
            (1, -2), (1, 2), (1, -2), (-1, 2)
        ]

        # start at the top-left corner 0,0
        queue = deque([(0, 0, 0)]);  visited = {(0, 0)}

        while queue:
            row, col, move = queue.popleft()
            if (row, col) == (x,y):
                return move

            for dr, dc in directions:
                r, c = row + dr, col + dc
                # if 0 <= r < 200 and 0 <= c < 200 and (r, c) not in visited:
                # no need to check grid bound, since its infinite
                if (r, c) not in visited:
                    visited.add((r, c))
                    queue.append((r, c, move+1))
        return -1
    # section:problem-1:end

    # ============================
    # section:problem-994-hi:start
    # section:problem-994-hi:end

    # section:problem-994:start
    # in progress ... 🔺
    def orangesRotting(self, grid: list[list[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        direction = [(1,0), (-1,0), (0,1), (0,-1)] # L R U D
        # BFS
        visited = {(0,0)}
        arr = [(0,0)]; queue = deque(arr)
        minute = -1

        while queue: # Fifo
            minute += 1  # Each iteration represents one minute
            x,y = queue.popleft()
            #if grid[x][y] == 2:

            level_size = len(queue)
            if grid[x][y] == 2: pass

            # === level start ===
            for _ in range(level_size):

                for dx,dy in direction:
                    nx,ny = x+nx, y+ny
                    if (nx,ny) not in visited and ( 0 <= nx < row and 0 <= ny < col) :
                        visited.add((nx,ny))
                        if grid[nx][ny] != 0:
                            queue.append((nx,ny))
            # === level end ===

        return minute
    # section:problem-994:end

    # ============================
    # section:problem-542:start
    # section:problem-542:end

    # section:problem-542-hi:start
    def updateMatrix(self, mat):
        # Multi-source BFS: start from all 0s simultaneously to find nearest distances
        from collections import deque

        rows, cols = len(mat), len(mat[0])
        output = [[-1] * cols for _ in range(rows)]  # Initialize with -1 for unvisited
        queue = deque()  # BFS queue for processing

        # ⭐Step 1: Initialize the queue with all the 0 cells
        # set their distance to 0 in the output grid
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    queue.append((r, c))  # Add all 0 positions to queue
                    output[r][c] = 0      # Distance to itself is 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
        for i in range(rows): print(output[i])
        print(queue)

        # ⭐Step 2: Perform BFS traversal level by level
        distance = 1
        while queue:
            # Process all cells at current distance level
            #print(f"\n{'\t'} level: {distance}")
            for _ in range(len(queue)):
                r, c = queue.popleft()
                #print(f"{'\t'} pop: ({r},{c}) | {output[r][c]} | Queue: {queue}")
                # Check all 4 neighboring cells
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    # If neighbor is within bounds and unvisited
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if output[nr][nc] == -1:
                            output[nr][nc] = distance  # Set distance to current level
                            queue.append((nr, nc))     # Add to queue for next level
                            #print(f"{'\t'} append: ({nr},{nc}) | {output[nr][nc]} | Queue: {queue}")
            distance += 1  # Increment distance for next level
            #for i in range(rows): print(output[i])

        return output
    # section:problem-542-hi:end

    # section:problem-542-hi-console:start
    """
    [-1, 0, -1]
    [0, -1, 0]
    [-1, -1, -1]
    deque([(0, 1), (1, 0), (1, 2)])
    
         level: 1
         pop: (0,1) | 0 | Queue: deque([(1, 0), (1, 2)])
         append: (0,2) | 1 | Queue: deque([(1, 0), (1, 2), (0, 2)])
         append: (1,1) | 1 | Queue: deque([(1, 0), (1, 2), (0, 2), (1, 1)])
         append: (0,0) | 1 | Queue: deque([(1, 0), (1, 2), (0, 2), (1, 1), (0, 0)])
         pop: (1,0) | 0 | Queue: deque([(1, 2), (0, 2), (1, 1), (0, 0)])
         append: (2,0) | 1 | Queue: deque([(1, 2), (0, 2), (1, 1), (0, 0), (2, 0)])
         pop: (1,2) | 0 | Queue: deque([(0, 2), (1, 1), (0, 0), (2, 0)])
         append: (2,2) | 1 | Queue: deque([(0, 2), (1, 1), (0, 0), (2, 0), (2, 2)])
    [1, 0, 1]
    [0, 1, 0]
    [1, -1, 1]
    
         level: 2
         pop: (0,2) | 1 | Queue: deque([(1, 1), (0, 0), (2, 0), (2, 2)])
         pop: (1,1) | 1 | Queue: deque([(0, 0), (2, 0), (2, 2)])
         append: (2,1) | 2 | Queue: deque([(0, 0), (2, 0), (2, 2), (2, 1)])
         pop: (0,0) | 1 | Queue: deque([(2, 0), (2, 2), (2, 1)])
         pop: (2,0) | 1 | Queue: deque([(2, 2), (2, 1)])
         pop: (2,2) | 1 | Queue: deque([(2, 1)])
    [1, 0, 1]
    [0, 1, 0]
    [1, 2, 1]
    
         level: 3
         pop: (2,1) | 2 | Queue: deque([])
    [1, 0, 1]
    [0, 1, 0]
    [1, 2, 1]
    """
    # section:problem-542-hi-console:end

    # section:problem-815:start
    # section:problem-815:end


if __name__ == "__main__":
    mat = [
        [1, 0, 1],
        [0, 1, 0],
        [1, 1, 1],
    ]

    Solution().updateMatrix(mat)