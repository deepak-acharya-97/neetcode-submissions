# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def approach1():
            def util(node):
                if not node:
                    return node

                node.left, node.right = node.right, node.left

                util(node.left)
                util(node.right)

                return node

            return util(root)

        return approach1()
