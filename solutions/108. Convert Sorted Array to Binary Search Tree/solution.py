# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, nums):
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])
        mid = math.ceil(len(nums) / 2) - 1
        return TreeNode(nums[mid], self.solve(nums[:mid]), self.solve(nums[mid + 1 :]))

    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self.solve(nums)