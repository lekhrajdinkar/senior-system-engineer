# ============ DFS on graph : 2d matrix ====
from typing import List

# section::DFS-template-1::start
def maxValue(node):
    # empty L/R subtree
    if node is None:
        return

    # leaf node cases:
    # eg: need to calculate sum all the till leaf. ⭐⭐⭐⭐⭐
    # eg: print max leaf node
    if node.left is None and node.right is None:
        print(node.val)

    maxValue(node.left)
    maxValue(node.right)
    #return 1 + max(left, right) # longest path

# section::DFS-template-1::end

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