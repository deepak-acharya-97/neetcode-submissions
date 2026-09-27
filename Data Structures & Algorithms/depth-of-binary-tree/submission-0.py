# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def util(node):
            if not node:
                return 0
            
            left = util(node.left)
            right = util(node.right)
            
            return 1 + max(left, right)
        
        return util(root)
