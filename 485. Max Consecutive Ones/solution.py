class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        soFar = 0
        maxSoFar = 0
        for i in nums:
            if i == 1:
                soFar += 1
                maxSoFar = max(maxSoFar, soFar)
            else:
                soFar = 0
        return maxSoFar