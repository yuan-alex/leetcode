class Solution:
  def reverseWords(self, s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    s.reverse()
    left, right = 0, 0
    while True:
      if right == len(s):
        s[left:right] = s[left:right][::-1]
        break
      elif right == len(s) or s[right] == " ":
        s[left:right] = s[left:right][::-1]
        right += 1
        left = right
      else:
        right += 1
