class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        unique = set(nums)
        majorityThreshold = len(nums) / 2
        for i in unique:
            if nums.count(i) > majorityThreshold:
                return i
