class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts = {}
        for i, c in enumerate(s):
            if c in counts:
                counts[c] += 1
            else:
                counts[c] = 1
        for i in counts:
            if counts[i] == 1:
                return s.index(i)
        return -1