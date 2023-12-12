class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = collections.Counter(arr)
        return len(counts.values()) == len(set(counts.values()))