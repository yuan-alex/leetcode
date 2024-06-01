class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        for i in range(len(word) - len(ch) + 1):
            if word[i:i + len(ch)] == ch:
                return word[:i+1][::-1] + word[i+1:]
        return word
