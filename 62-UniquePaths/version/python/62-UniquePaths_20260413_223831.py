# Last updated: 4/13/2026, 10:38:31 PM
1class Solution:
2    def uniquePaths(self, m: int, n: int) -> int:
3
4        dp = [[-1] * n for _ in range(m)]
5
6        dp[0][0] = 1
7
8        for j in range(n):
9            dp[0][j] = 1
10
11        for i in range(m):
12            dp[i][0] = 1
13
14        for i in range(1, m):
15            for j in range(1, n):
16                dp[i][j] = dp[i][j- 1] + dp[i - 1][j]
17
18
19        return dp[m - 1][n - 1] 
20        