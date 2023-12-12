class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        unique = set(nums)
        largest = max(unique)
        unique.remove(largest)
        secondLargest = max(unique)
        if secondLargest * 2 > largest:
            return -1
        return nums.index(largest)
