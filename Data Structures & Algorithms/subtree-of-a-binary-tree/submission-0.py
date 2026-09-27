"""
https://neetcode.io/problems/subtree-of-a-binary-tree
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        def same_tree_util(node1, node2):
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
            return node1.val == node2.val and same_tree_util(node1.left, node2.left) and same_tree_util(node1.right, node2.right)

        def issubtreeutil(node):
            if not node:
                return False
            if node.val == subRoot.val and same_tree_util(node, subRoot):
                return True
            return issubtreeutil(node.left) or issubtreeutil(node.right)
        
        return issubtreeutil(root)

