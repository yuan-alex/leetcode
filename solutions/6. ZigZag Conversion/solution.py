class Solution:
  def convert(self, s: str, numRows: int) -> str:
    if numRows == 1:
      return s
    rows = {i: [] for i in range(numRows)}
    r, direction = 0, 1
    for i, c in enumerate(s):
      rows[r].append(c)
      r += direction
      if r == 0 or r == numRows - 1:
        direction *= -1
    return "".join(["".join(i) for i in rows.values()])
