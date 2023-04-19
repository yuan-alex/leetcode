class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        sol = "".join([i[0] + i[1] for i in zip(word1, word2)])
        if len(word1) > len(word2):
            sol += word1[len(word2):]
        elif len(word2) > len(word1):
            sol += word2[len(word1):]
        return sol
