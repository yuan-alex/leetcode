class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        slider = {}
        for left in range(0, len(s)):
            slider = {}
            for right in range(left, len(s)):
                if s[right] in slider:
                    break
                slider[s[right]] = True
                maxLength = max(maxLength, len(slider))
        return maxLength