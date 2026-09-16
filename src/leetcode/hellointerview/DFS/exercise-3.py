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


    # section::section-200::start
    def section_200(self, matrics: List[List[int]]):
        pass
    # section::section-200::end


    # section::section-733::start
    # Flood-fill
    def flood_fill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
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


            for dr, dc in directions: # DFS on neighbour run max 4 times
                dfs_helper(r + dr, c + dc, depth+1)

        dfs_helper(sr, sc, 1) # start from given point

        return image
    # section::section-733::end

    # section::section-130::start
    # section::section-130::end

    # section::section-417::start
    # section::section-417::end


# ===============

if __name__ == "__main__":
    def flood_fill_test():
        print('»'*30);Solution().flood_fill([[1,0,1],[1,0,0],[0,0,1]], 2,1,2)
        print('»'*30);Solution().flood_fill([[2,2,2],[2,2,0],[2,0,1]], 1,1,3)
        print('»'*30);Solution().flood_fill( [[1,1,1],[1,1,0],[1,0,1]], 2,2,2)

    flood_fill_test()