# Last updated: 5/24/2026, 7:40:28 PM
1class Solution:
2    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
3        m, n = len(text1), len(text2)
4
5        @cache
6        def dfs(i, j):
7            if i < 0 or j < 0: return 0
8
9            if text1[i] == text2[j]:
10                return 1 + dfs(i - 1, j - 1)
11            else:
12                return max(dfs(i - 1, j), dfs(i, j - 1))
13
14        
15        return dfs(m - 1, n - 1)
16        
17
18        