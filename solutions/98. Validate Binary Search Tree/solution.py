# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, node, max, min):
        if node is None:
            return True
        if node.val >= max or node.val <= min:
            return False
        return self.traverse(node.left, node.val, min) and self.traverse(
            node.right, max, node.val
        )

    def isValidBST(self, root: TreeNode) -> bool:
        return self.traverse(root, math.inf, -math.inf)