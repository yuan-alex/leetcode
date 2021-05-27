# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, node, isLeft):
        if not node:
            return 0
        if not node.left and not node.right and isLeft:
            return node.val
        return self.traverse(node.left, True) + self.traverse(node.right, False)

    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        return self.traverse(root, False)