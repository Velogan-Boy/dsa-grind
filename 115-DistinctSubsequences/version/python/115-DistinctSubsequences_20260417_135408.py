# Last updated: 4/17/2026, 1:54:08 PM
1class Solution:
2    def numDistinct(self, s: str, t: str) -> int:
3        m,n = len(s), len(t)
4
5        dp = [[0] * (n + 1) for _ in range(m + 1)]
6
7        for i in range(m + 1):
8            dp[i][n] = 1
9
10        for i in range(m - 1, -1, -1):
11            for j in range(n - 1, -1, -1):
12                if s[i] == t[j]:
13                    dp[i][j] = dp[i + 1][j + 1] + dp[i + 1][j]
14                else:
15                    dp[i][j] = dp[i+1][j]
16
17        
18        return dp[0][0]