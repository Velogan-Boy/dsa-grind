# Last updated: 5/31/2026, 12:23:36 AM
1class Solution:
2    def climbStairs(self, n: int) -> int:
3
4        @cache
5        def dfs(n):
6            if n == 0 or n == 1: return 1
7
8            return dfs(n - 1) + dfs(n - 2)
9
10        return dfs(n)
11
12        
13        