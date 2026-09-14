from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def array_to_tree(arr) -> Optional[TreeNode]:

    if not arr or arr[0] is None:
        return None

    root = TreeNode(arr[0])
    queue = deque([root])
    i = 1

    while queue and i < len(arr):

        current = queue.popleft()

        # Left
        if i < len(arr) and arr[i] is not None:
            current.left = TreeNode(arr[i])
            queue.append(current.left)
        i += 1

        # Right
        if i < len(arr) and arr[i] is not None:
            current.right = TreeNode(arr[i])
            queue.append(current.right)
        i += 1

    draw_tree(root)
    return root


def draw_tree(node, prefix="", is_left=True):

    if node is None:
        return

    # Print right subtree first
    if node.right:
        draw_tree(
            node.right,
            prefix + ("│   " if is_left else "    "),
            False
        )

    # Print current node
    print(prefix + ("└── " if is_left else "┌── ") + str(node.val))

    # Print left subtree
    if node.left:
        draw_tree(
            node.left,
            prefix + ("    " if is_left else "│   "),
            True
        )