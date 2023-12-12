class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        while len(nums) > 1:
            nums = [(n + nums[i + 1]) % 10 for i, n in enumerate(nums[:-1])]
        return nums[0]
