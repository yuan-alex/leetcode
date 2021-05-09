# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverseNode(self, node: TreeNode, array, stringSoFar):
        stringSoFar += str(node.val) + "->"
        if node.left:
            self.traverseNode(node.left, array, stringSoFar)
        if node.right:
            self.traverseNode(node.right, array, stringSoFar)
        if not node.left and not node.right:
            array.append(stringSoFar[:-2])

    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        array = []
        self.traverseNode(root, array, "")
        return array