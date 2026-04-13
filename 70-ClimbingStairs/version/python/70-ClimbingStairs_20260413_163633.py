# Last updated: 4/13/2026, 4:36:33 PM
1class Solution:
2    def climbStairs(self, n: int) -> int:
3        dp = [0] * (n + 1)
4        
5        dp[0] = 1
6        dp[1] = 1
7        
8        for i in range(2, n + 1):
9            dp[i] = dp[i - 1] + dp[i - 2]
10        
11        return dp[n]