# Last updated: 4/15/2026, 7:49:27 PM
1class Solution:
2    def longestPalindromeSubseq(self, s: str) -> int:
3        return self.lcs(s, s[::-1])
4
5
6    def lcs(self, str1, str2):
7        m,n = len(str1), len(str2)
8
9        @cache
10        def dfs(i, j):
11            if i < 0 or j < 0: return 0
12
13            if str1[i] == str2[j]:
14                return 1 + dfs(i - 1, j - 1)
15            else:
16                return max(dfs(i - 1, j), dfs(i, j - 1))
17            
18        return dfs(m - 1, n - 1)
19