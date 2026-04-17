# Last updated: 4/17/2026, 1:48:46 PM
1class Solution:
2    def numDistinct(self, s: str, t: str) -> int:
3        m,n = len(s), len(t)
4
5        @cache
6        def dfs(i, j):
7            if j == n:
8                return 1
9
10            if i == m:
11                return 0
12            
13            if s[i] == t[j]:
14                return dfs(i + 1, j + 1) + dfs(i + 1, j)
15            else:
16                return dfs(i + 1, j)
17        
18        return dfs(0, 0)