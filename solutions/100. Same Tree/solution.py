# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, pNode, qNode):
        if not pNode and not qNode:
            return True
        if not pNode and qNode or pNode and not qNode or pNode.val != qNode.val:
            return False
        return self.traverse(pNode.left, qNode.left) and self.traverse(
            pNode.right, qNode.right
        )

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        return self.traverse(p, q)