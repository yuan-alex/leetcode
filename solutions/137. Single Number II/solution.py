class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counts = {}
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
            if counts[num] == 3:
                counts.pop(num)
        return list(counts.keys())[0]
