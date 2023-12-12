class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        history = {}
        for i, num in enumerate(nums):
            if target - num in history:
                return [i, history[target - num]]
            history[num] = i