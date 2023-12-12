class Solution:
  def shortestWay(self, source: str, target: str) -> int:
    indexes = {}
    for i, c in enumerate(source):
      if c in indexes:
        indexes[c].append(i)
      else:
        indexes[c] = [i]

    sol, sourceIndex = 1, 0
    window = indexes.copy()
    for i, c in enumerate(target):
      if c not in indexes:
        return -1

      if len(window[c]) == 0 or max(window[c]) < sourceIndex:
        sol += 1
        window = indexes.copy()
        sourceIndex = 0

      window[c] = [i for i in window[c] if i >= sourceIndex]
      sourceIndex = window[c][0]
      window[c] = window[c][1:]

    return sol
