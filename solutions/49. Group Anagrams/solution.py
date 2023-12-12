class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        unique = {"".join(sorted(i)): [] for i in strs}
        for i in strs:
            unique["".join(sorted(i))].append(i)
        return unique.values()
