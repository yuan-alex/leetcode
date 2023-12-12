import collections


class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts = collections.Counter(s)
        for i in counts:
            if counts[i] == 1:
                return s.index(i)
        return -1