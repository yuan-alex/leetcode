# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, t1, t2):
        if not t1 and not t2:
            return True
        if not t1 or not t2 or t1.val != t2.val:
            return False
        return self.traverse(t1.left, t2.right) and self.traverse(t1.right, t2.left)

    def isSymmetric(self, root: TreeNode) -> bool:
        return self.traverse(root.left, root.right)