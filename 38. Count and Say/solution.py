class Solution:
    def countAndSay(self, n: int) -> str:
        def say(s: str):
            sol, left, right = "", 0, 0
            while right < len(s):
                if s[left] == s[right]:
                    right += 1
                if right == len(s) or s[left] != s[right]:
                    sol += "{}{}".format(right - left, s[left])
                    left = right
            return sol
        
        def recursive(n: int) -> str:
            if n == 1:
                return "1"
            return say(recursive(n - 1))
        
        return recursive(n)
