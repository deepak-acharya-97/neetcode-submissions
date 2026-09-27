"""
https://neetcode.io/problems/binary-tree-maximum-path-sum
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        self.result = root.val

        def dfs(node):
            if not node:
                return 0

            left_max_path = max(dfs(node.left), 0)
            right_max_path = max(dfs(node.right), 0)

            self.result = max(self.result, node.val + left_max_path + right_max_path)

            return node.val + max(left_max_path, right_max_path)
        
        dfs(root)
        return self.result


