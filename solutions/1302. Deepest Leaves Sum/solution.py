# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        nodes = [root]
        while nodes:
            new = []
            for i in nodes:
                if i.left:
                    new.append(i.left)
                if i.right:
                    new.append(i.right)
            prev, nodes = nodes, new
        deepestSum = 0
        for i in prev:
            deepestSum += i.val
        return deepestSum