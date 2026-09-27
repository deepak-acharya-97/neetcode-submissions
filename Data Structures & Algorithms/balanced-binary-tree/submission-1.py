"""
http://neetcode.io/problems/balanced-binary-tree
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node):
            if not node:
                return 0
            left = height(node.left)
            right = height(node.right)

            return 1 + max(left, right)
        def is_balanced_util(node):
            if not node:
                return True
            if not node.left and not node.right:
                return True
            left = height(node.left)
            right = height(node.right)
            
            result = True if abs(left - right) <= 1 else False
            return result and is_balanced_util(node.left) and is_balanced_util(node.right)

        return is_balanced_util(root)


