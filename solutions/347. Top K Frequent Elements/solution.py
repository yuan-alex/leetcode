import collections


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = collections.Counter(nums)
        sortedCounts = dict(sorted(counts.items(), key=lambda x: x[1], reverse=True))
        return list(sortedCounts.keys())[:k]