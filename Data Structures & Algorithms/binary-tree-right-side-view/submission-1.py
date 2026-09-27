# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result_map = {}

        def util(node, level):
            if not node:
                return

            if level not in result_map:
                result_map[level] = node.val

            util(node.right, level + 1)
            util(node.left, level + 1)

        util(root, 0)
        return list(result_map.values())

