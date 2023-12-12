# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, tree1, tree2):
        if tree1 is None or tree2 is None:
            return tree1 == tree2
        return tree1.val == tree2.val and self.isSameTree(tree1.left, tree2.left) and self.isSameTree(tree1.right, tree2.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        if self.isSameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
