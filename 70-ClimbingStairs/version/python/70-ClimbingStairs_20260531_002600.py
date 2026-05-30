# Last updated: 5/31/2026, 12:26:00 AM
1class Solution:
2    def climbStairs(self, n: int) -> int:
3
4        dp = [1] * (n + 1)
5
6        for i in range(2, n + 1):
7            dp[i] = dp[i-1] + dp[i-2]
8
9
10        return dp[n]
11
12
13        
14        