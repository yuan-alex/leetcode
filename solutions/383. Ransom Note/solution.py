class Solution:
  def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    ransomDict = collections.Counter(ransomNote)
    magazineDict = collections.Counter(magazine)
    for i, j in ransomDict.items():
      if i not in magazineDict or magazineDict[i] < j:
        return False
    return True
