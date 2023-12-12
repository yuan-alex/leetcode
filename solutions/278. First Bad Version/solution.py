# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
      left = 1
      right = n
      while left < right:
        mid = left + (right - left) // 2
        print(mid)
        if isBadVersion(mid):
          # first worse is below us
          right = mid
        else:
          # first worse is above us
          left = mid + 1
      return left