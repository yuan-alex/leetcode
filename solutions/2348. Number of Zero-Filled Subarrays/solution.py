class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        total, window = 0, 0
        for i in range(len(nums)):
            if nums[i] == 0:
                window += 1
            else:
                window = 0
            total += window
        return total
