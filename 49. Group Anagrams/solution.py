class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        unique = {}
        for i in range(0, len(strs)):
            string = list(strs[i])
            string.sort()
            string = str(string)
            if string in unique:
                unique[string].append(strs[i])
            else:
                unique[string] = [strs[i]]
        return unique.values()