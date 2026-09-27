# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def is_valid_util(node, min_limit, max_limit):
            if not node:
                return True

            if not (min_limit < node.val < max_limit):
                print(f"{min_limit=}, {max_limit=}, {node.val}")
                return False

            return is_valid_util(node.left, min_limit, node.val) and is_valid_util(node.right, node.val, max_limit)

        return is_valid_util(root, float("-inf"), float("inf"))
