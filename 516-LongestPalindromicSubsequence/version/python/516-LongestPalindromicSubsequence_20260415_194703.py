# Last updated: 4/15/2026, 7:47:03 PM
1class Solution:
2    def longestPalindromeSubseq(self, s: str) -> int:
3        return self.lcs(s, s[::-1])
4
5
6    @cache
7    def lcs(self, str1, str2):
8        m,n = len(str1), len(str2)
9
10        memo = [[-1] * n for _ in range(m)]
11
12        def dfs(i, j):
13            if i < 0 or j < 0: return 0
14
15            if memo[i][j] != -1: return memo[i][j]
16
17            if str1[i] == str2[j]:
18                memo[i][j] =  1 + dfs(i - 1, j - 1)
19            else:
20                memo[i][j] = max(dfs(i - 1, j), dfs(i, j - 1))
21            
22            return memo[i][j]
23        
24        return dfs(m - 1, n - 1)
25