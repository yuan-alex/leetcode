class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n for i in range(m)]
        dp[0][0] = 1
        for row in range(0, m):
            for col in range(0, n):
                if obstacleGrid[row][col] == 1:
                    continue
                if col - 1 >= 0 and obstacleGrid[row][col - 1] == 0:
                    dp[row][col] += dp[row][col - 1]
                if row - 1 >= 0 and obstacleGrid[row - 1][col] == 0:
                    dp[row][col] += dp[row - 1][col]
        return dp[m - 1][n - 1]