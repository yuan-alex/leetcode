class Solution:
    def convert(self, s: str, numRows: int) -> str:
        strings = {i: [] for i in range(0, numRows)}
        increasing = True
        row = 0
        for i in s:
            strings[row].append(i)
            if numRows == 1:
                continue
            if increasing:
                row += 1
            else:
                row -= 1
            if row == -1 or row == numRows:
                if increasing:
                    row -= 2
                else:
                    row += 2
                increasing = not increasing
        ans = ""
        for i in strings.values():
            ans += "".join(i)
        return ans