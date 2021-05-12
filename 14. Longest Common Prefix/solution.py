class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        prefix = strs[0]
        for i in range(1, len(strs)):
            newPrefix = ""
            for j in range(0, len(strs[i])):
                if j < len(prefix) and prefix[j] == strs[i][j]:
                    newPrefix += prefix[j]
                else:
                    break
            prefix = newPrefix
        return prefix