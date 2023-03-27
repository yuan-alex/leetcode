class Solution:
    def checkRecord(self, s: str) -> bool:
        if s.count("A") >= 2:
            return False
        if len(s) < 3:
            return True
        for i in range(2, len(s)):
            if s[i] == s[i - 1] and s[i] == s[i - 2] and s[i] == "L":
                return False
        return True
