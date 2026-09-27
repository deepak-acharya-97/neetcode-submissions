# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.result = 0

        def util(node):
            if node is None:
                return 0
            
            left = util(node.left)
            right = util(node.right)

            self.result = max(self.result, left + right)

            return 1 + max(left, right)

        util(root)

        return self.result
        