class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ideal_sum = 0
        actual_sum = 0
        for i in range(0, len(nums)):
            ideal_sum += i
            actual_sum += nums[i]
        ideal_sum += len(nums)
        return ideal_sum - actual_sum