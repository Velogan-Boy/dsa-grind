# Last updated: 6/25/2026, 2:04:09 PM
1class Solution:
2    def uniquePaths(self, m: int, n: int) -> int:
3
4        @cache
5        def dfs(i, j):
6            if i == m - 1 and j == n - 1: return 1
7
8            if i > m - 1 or j > n - 1: return 0
9
10            return dfs(i + 1, j) + dfs(i, j + 1)
11
12        return dfs(0,0)
13
14
15
16
17        