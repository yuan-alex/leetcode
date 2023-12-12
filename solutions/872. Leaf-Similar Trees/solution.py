# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, root):
        if root.left and root.right:
            return self.traverse(root.left) + self.traverse(root.right)
        elif root.left:
            return self.traverse(root.left)
        elif root.right:
            return self.traverse(root.right)
        else:
            return [root.val]

    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        return self.traverse(root1) == self.traverse(root2)