# Last updated: 4/13/2026, 4:35:44 PM
1class Solution:
2    def climbStairs(self, n: int) -> int:
3        dp = [-1] * (n + 1)
4
5        def dfs(n):
6            if n < 0:
7                return 0
8
9            if n == 0 or n == 1:
10                return 1
11            
12            if dp[n] != -1:
13                return dp[n]
14            
15            dp[n] = dfs(n - 1) + dfs(n - 2)
16            return dp[n]
17        
18        return dfs(n)