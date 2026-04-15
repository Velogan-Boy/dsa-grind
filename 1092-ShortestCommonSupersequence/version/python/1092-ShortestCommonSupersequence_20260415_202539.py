# Last updated: 4/15/2026, 8:25:39 PM
1class Solution:
2    def lcs_dp(self, A, B):
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
15    def shortestCommonSupersequence(self, A: str, B: str) -> str:
16        dp = self.lcs_dp(A, B)
17        i, j = len(A), len(B)
18        res = []
19
20        while i > 0 and j > 0:
21            if A[i-1] == B[j-1]:
22                res.append(A[i-1])
23                i -= 1
24                j -= 1
25            elif dp[i-1][j] > dp[i][j-1]:
26                res.append(A[i-1])
27                i -= 1
28            else:
29                res.append(B[j-1])
30                j -= 1
31
32        while i > 0:
33            res.append(A[i-1])
34            i -= 1
35        while j > 0:
36            res.append(B[j-1])
37            j -= 1
38
39        return "".join(reversed(res))