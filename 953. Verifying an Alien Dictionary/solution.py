class Solution:
    def isSorted(self, word1, word2, order):
        shortestLength = min(len(word1), len(word2))
        for i in range(0, shortestLength):
            if word1[i] == word2[i]:
                continue
            if order.index(word1[i]) < order.index(word2[i]):
                return True
            return False
        return len(word1) <= len(word2)

    def isAlienSorted(self, words: List[str], order: str) -> bool:
        for i in range(0, len(words) - 1):
            if not self.isSorted(words[i], words[i + 1], order):
                return False
        return True