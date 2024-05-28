# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def traverse(node, height):
            if node is None:
                return True, height
            currentHeight = height + 1
            leftValid, leftHeight = traverse(node.left, currentHeight)
            rightValid, rightHeight = traverse(node.right, currentHeight)
            if not leftValid or not rightValid or abs(leftHeight - rightHeight) > 1:
                return False, 0
            return True, max(leftHeight, rightHeight)
        valid, _ = traverse(root, 0)
        return valid
