import collections


class Solution:
    def frequencySort(self, s: str) -> str:
        counts = collections.Counter(s)
        sortedCounts = dict(sorted(counts.items(), key=lambda x: x[1], reverse=True))
        sortedString = ""
        for i in sortedCounts:
            sortedString += i * sortedCounts[i]
        return sortedString