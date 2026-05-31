# Last updated: 5/31/2026, 11:00:12 PM
1class Solution:
2    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
3
4        m, n = len(s1), len(s2)
5
6        if m + n != len(s3):
7            return False
8
9        dp = [[False] * (n + 1) for _ in range(m + 1)]
10
11        dp[0][0] = True
12
13        for i in range(1, m + 1):
14            dp[i][0] = (
15                dp[i - 1][0]
16                and s1[i - 1] == s3[i - 1]
17            )
18
19        for j in range(1, n + 1):
20            dp[0][j] = (
21                dp[0][j - 1]
22                and s2[j - 1] == s3[j - 1]
23            )
24
25        for i in range(1, m + 1):
26            for j in range(1, n + 1):
27
28                dp[i][j] = (
29                    dp[i - 1][j]
30                    and s1[i - 1] == s3[i + j - 1]
31                ) or (
32                    dp[i][j - 1]
33                    and s2[j - 1] == s3[i + j - 1]
34                )
35
36        return dp[m][n]