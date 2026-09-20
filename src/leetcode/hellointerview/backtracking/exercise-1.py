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

    # section:problem-79-DFS-1:start
    # 🔺Issue1: always start at (0, 0)
    def exist1(self, board: list[list[str]], word: str) -> bool:
        visited = set() # tuple (x,y) coordinate
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        count = 0
        nextChar = word[0]

        def helper(r, c):
            nonlocal count
            nonlocal nextChar
            if (r, c) in visited: return # already visited
            if (r < 0 or r >= len(board))   or   (c < 0 or c >= len(board[0])): return # matrix bound
            if board[r][c] != nextChar : return

            visited.add((r, c))

            print(f"Found {nextChar} at {r},{c}")
            count += 1
            if  count < len(word):
                nextChar = word[count]
                for dr, dc in directions:  # DFS on neighbour
                    helper(r + dr, c + dc)

        helper(0, 0) # 🔺
        return True if count == len(word) else False
    # section:problem-79-DFS-1:end

    # section:problem-79-DFS-2:start
    # Working.
    # - try every starting cell
    # - create a fresh visited for each starting point
    def exist_dfs_2(self, board: list[list[str]], word: str) -> bool:
        rows = len(board); cols = len(board[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        #for r in range(rows): print(board[r]) # print board

        def helper(r, c, count, nextChar, visited ):
            if (r, c) in visited: return # already visited
            if (r < 0 or r >= len(board))   or   (c < 0 or c >= len(board[0])): return # matrix bound
            if board[r][c] != nextChar and len(visited) > 0  : return #  backtrack

            visited.add((r, c))

            print(f"- Found {nextChar} at {r},{c} | count : {count}")
            count += 1
            if count == len(word): return # reached max, so exit recursion
            else:
                for dr, dc in directions:  # DFS on neighbour
                    helper(r + dr, c + dc, count, word[count], visited)

        # Try all start point
        stepCount=0
        for r in range(rows):
            for c in range(cols):
                stepCount += 1
                print(f"✔️ step: {stepCount}/{rows*cols} | stating point: {r},{c}")
                visited = set() # create new visited set for each starting point execution
                helper(r, c, 0, word[0], visited)
                if len(visited)  == len(word):
                    print(f"{word} found ✅"); return True # early return

        print(f"{word} not found 🔺"); return False # eventually False fallback
    # section:problem-79-sol2:end

    # section:problem-79-BACKT-1-hi:start
    # Did nt understand
    def exist_backt_1(self, board: list[list[str]], word: str) -> bool:
        pass
    # section:problem-79-BACKT-1-hi:end

    # section:problem-78:start
    def problem78(self, root, target):
        pass
    # section:problem-78:end

    # section:problem-22:start
    def problem22(self, root, target):
        pass
    # section:problem-22:end

    # section:problem-39:start
    def problem39(self, root, target):
        pass
    # section:problem-39:end

    # section:problem-131:start
    def problem131(self, root, target):
        pass
    # section:problem-131:end

    # section:problem-51:start
    def problem51(self, root, target):
        pass
    # section:problem-51:end

# ---------------------------
if __name__ == "__main__":
    #Solution().pathSum(array_to_tree([5,4,8,11,None,13,4,7,2,None,None,5,1]), 22)

    grid1 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    def test79_dfs():
        print('-'*50, "ABCCED");Solution().exist_dfs_2(grid1,"ABCCED")
        print('-'*50,"SEE");Solution().exist_dfs_2(grid1,"SEE")
        print('-'*50,"ABCB");Solution().exist_dfs_2(grid1,"ABCB")
        print('-'*50,"BA");Solution().exist_dfs_2( [["A","X","B"]],"BA")

    def test79_backT():
        print('-'*50, "ABCCED");Solution().exist_backt_1(grid1,"ABCCED")
        print('-'*50,"SEE");Solution().exist_backt_1(grid1,"SEE")
        print('-'*50,"ABCB");Solution().exist_backt_1(grid1,"ABCB")

    test79_dfs() # working
    #test79_backT()