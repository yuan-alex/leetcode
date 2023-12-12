class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        shortestDistance = math.inf

        p1 = -1
        p2 = -1
        for i, word in enumerate(wordsDict):
            if word == word1:
                p1 = i
            elif word == word2:
                p2 = i
            if p1 >= 0 and p2 >= 0:
                shortestDistance = min(shortestDistance, abs(p2 - p1))
        return shortestDistance