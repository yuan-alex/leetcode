# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, node1, node2):
        if not node1 and not node2:
            return None
        if not node1:
            return node2
        if not node2:
            return node1
        myNode = TreeNode()
        myNode.val = node1.val + node2.val
        myNode.left = self.traverse(node1.left, node2.left)
        myNode.right = self.traverse(node1.right, node2.right)
        return myNode

    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        return self.traverse(t1, t2)