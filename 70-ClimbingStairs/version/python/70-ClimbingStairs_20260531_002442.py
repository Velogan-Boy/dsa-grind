# Last updated: 5/31/2026, 12:24:42 AM
1class Solution:
2    def climbStairs(self, n: int) -> int:
3
4        dp = [-1] * (n + 1)
5
6        def dfs(n):
7            if n == 0 or n == 1: return 1
8
9            if dp[n] != -1: return dp[n]
10
11            dp[n] = dfs(n - 1) + dfs(n - 2)
12
13            return dp[n]
14
15        return dfs(n)
16
17        
18        