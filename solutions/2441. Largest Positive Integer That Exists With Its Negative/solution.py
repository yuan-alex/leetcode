class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        largestSeen = -1
        seen = set()
        for i in nums:
            if -1 * i in seen:
                largestSeen = max(largestSeen, abs(i))
            seen.add(i)
        return largestSeen
