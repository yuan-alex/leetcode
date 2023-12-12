class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        result = []
        unique = set(nums)
        threshold = len(nums) / 3
        for i in unique:
            if nums.count(i) > threshold:
                result.append(i)
        return result