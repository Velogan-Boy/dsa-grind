# Last updated: 4/15/2026, 7:46:43 PM
1class Solution:
2    def longestPalindromeSubseq(self, s: str) -> int:
3        return self.lcs(s, s[::-1])
4
5
6    def lcs(self, str1, str2):
7        m,n = len(str1), len(str2)
8
9        memo = [[-1] * n for _ in range(m)]
10
11        def dfs(i, j):
12            if i < 0 or j < 0: return 0
13
14            if memo[i][j] != -1: return memo[i][j]
15
16            if str1[i] == str2[j]:
17                memo[i][j] =  1 + dfs(i - 1, j - 1)
18            else:
19                memo[i][j] = max(dfs(i - 1, j), dfs(i, j - 1))
20            
21            return memo[i][j]
22        
23        return dfs(m - 1, n - 1)
24