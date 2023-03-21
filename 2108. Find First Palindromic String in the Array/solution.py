class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        sol = list(filter(lambda x: x == x[::-1], words))
        return sol[0] if len(sol) > 0 else ""
