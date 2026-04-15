# Last updated: 4/15/2026, 8:24:20 PM
1class Solution:
2    def lcs_dp(A, B):
3        m, n = len(A), len(B)
4        dp = [[0]*(n+1) for _ in range(m+1)]
5
6        for i in range(1, m+1):
7            for j in range(1, n+1):
8                if A[i-1] == B[j-1]:
9                    dp[i][j] = 1 + dp[i-1][j-1]
10                else:
11                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
12
13        return dp
14        
15    def minInsertions(self, s: str) -> int:
16        t = s[::-1]
17        n = len(s)
18
19        prev = [0] * (n + 1)
20
21        for i in range(1, n + 1):
22            curr = [0] * (n + 1)
23            for j in range(1, n + 1):
24                if s[i - 1] == t[j - 1]:
25                    curr[j] = 1 + prev[j - 1]
26                else:
27                    curr[j] = max(prev[j], curr[j - 1])
28            prev = curr
29
30        lps = prev[n]
31        return n - lps