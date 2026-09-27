# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.result = 0

        def good_node_util(node, max_along_the_path):
            if not node:
                return

            if node.val >= max_along_the_path:
                self.result += 1

            new_max_along_the_path = max(max_along_the_path, node.val)

            good_node_util(node.left, new_max_along_the_path)
            good_node_util(node.right, new_max_along_the_path)

        good_node_util(root, root.val)
        return self.result
