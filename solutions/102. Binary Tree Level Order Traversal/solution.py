# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = []
        if not root:
            return ans
        pointer = [root]
        while pointer:
            new = []
            ans.append([i.val for i in pointer])
            for i in pointer:
                if i.left:
                    new.append(i.left)
                if i.right:
                    new.append(i.right)
            pointer = new
        return ans