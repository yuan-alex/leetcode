class Solution:
    def customSortString(self, order: str, str: str) -> str:
        output = ""
        strList = list(str)
        for i in order:
            cnt = strList.count(i)
            strList = [c for c in strList if c != i]
            output += i * cnt
        return output + "".join(strList)