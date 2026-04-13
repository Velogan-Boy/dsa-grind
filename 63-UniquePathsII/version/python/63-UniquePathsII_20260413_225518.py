# Last updated: 4/13/2026, 10:55:18 PM
1class Solution:
2    def uniquePathsWithObstacles(self, obstacleGrid):
3        m, n = len(obstacleGrid), len(obstacleGrid[0])
4
5        dp = [[0] * n for _ in range(m)]
6
7        for i in range(m):
8            if obstacleGrid[i][0] == 1:
9                break
10            dp[i][0] = 1
11
12        for j in range(n):
13            if obstacleGrid[0][j] == 1:
14                break
15            dp[0][j] = 1
16
17        for i in range(1, m):
18            for j in range(1, n):
19                if obstacleGrid[i][j] == 0:
20                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
21
22        return dp[m - 1][n - 1]