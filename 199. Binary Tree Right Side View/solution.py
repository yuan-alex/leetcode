# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        nodes = [root]
        ans = [root.val]
        while nodes:
            new = []
            for node in nodes:
                if node.left:
                    new.append(node.left)
                if node.right:
                    new.append(node.right)
            if new:
                ans.append(new[-1].val)
            nodes = new
        return ans
