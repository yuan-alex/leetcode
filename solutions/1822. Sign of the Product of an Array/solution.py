class Solution:
    def arraySign(self, nums: List[int]) -> int:
        if 0 in nums:
            return 0
        if len([i for i in nums if i < 0]) % 2 == 0:
            return 1
        return -1
