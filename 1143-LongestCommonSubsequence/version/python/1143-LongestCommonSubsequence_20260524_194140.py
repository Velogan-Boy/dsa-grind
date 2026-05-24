# Last updated: 5/24/2026, 7:41:40 PM
1class Solution:
2    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
3        m, n = len(text1), len(text2)
4
5        dp = [[-1] * n for _ in range(m)]
6
7        def dfs(i, j):
8            if i < 0 or j < 0: return 0
9            if dp[i][j] != -1: return dp[i][j]
10
11            if text1[i] == text2[j]:
12                dp[i][j] =  1 + dfs(i - 1, j - 1)
13            else:
14                dp[i][j] = max(dfs(i - 1, j), dfs(i, j - 1))
15
16            return dp[i][j]
17
18        
19        return dfs(m - 1, n - 1)
20        
21
22        