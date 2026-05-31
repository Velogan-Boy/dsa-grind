# Last updated: 5/31/2026, 11:03:12 PM
1class Solution:
2    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
3
4        m, n = len(s1), len(s2)
5
6        if m + n != len(s3):
7            return False
8
9        dp = [False] * (n + 1)
10
11        dp[0] = True
12
13        for j in range(1, n + 1):
14            dp[j] = dp[j - 1] and s2[j - 1] == s3[j - 1]
15
16        for i in range(1, m + 1):
17
18            dp[0] = dp[0] and s1[i - 1] == s3[i - 1]
19
20            for j in range(1, n + 1):
21
22                dp[j] = (
23                    (dp[j] and s1[i - 1] == s3[i + j - 1])
24                    or
25                    (dp[j - 1] and s2[j - 1] == s3[i + j - 1])
26                )
27
28        return dp[n]