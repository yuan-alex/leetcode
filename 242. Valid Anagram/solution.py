class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        listS = list(s)
        listS.sort()
        listT = list(t)
        listT.sort()
        return listS == listT