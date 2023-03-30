class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pointer = 0
        while pointer < min([len(i) for i in strs]):
            for i in range(len(strs) - 1):
                if strs[i][pointer] != strs[i+1][pointer]:
                    return strs[0][:pointer]
            pointer += 1
        return strs[0][:pointer]
