class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]
        ans = [[1], [1, 1]]
        for i in range(2, numRows):
            new = [1]
            for j in range(1, i):
                new.append(ans[i - 1][j - 1] + ans[i - 1][j])
            new.append(1)
            ans.append(new)
        return ans