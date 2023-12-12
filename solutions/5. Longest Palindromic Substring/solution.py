class Solution:
  def longestPalindrome(self, s: str) -> str:
    def expandAroundCenter(left, right) -> str:
      while left >= 0 and right < len(s) and s[left] == s[right]:
        left, right = left - 1, right + 1
      # we have to add 1 because the previous operation did one too many until it quit
      return s[left + 1:right]
    
    longest = ""
    for i in range(len(s)):
      singleChar = expandAroundCenter(i, i)
      twoChar = expandAroundCenter(i, i + 1)
      if len(singleChar) > len(twoChar):
        if len(singleChar) > len(longest):
          longest = singleChar
      else:
        if len(twoChar) > len(longest):
          longest = twoChar
    return longest
