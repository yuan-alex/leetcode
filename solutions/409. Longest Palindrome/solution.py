class Solution:
    def longestPalindrome(self, s: str) -> int:
        total = 0
        for i in collections.Counter(list(s)).values():
            total += i // 2 * 2
            if i % 2 == 1 and total % 2 == 0:
                total += 1
        return total