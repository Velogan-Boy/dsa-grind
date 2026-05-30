# Last updated: 5/31/2026, 12:28:19 AM
1class Solution:
2    def climbStairs(self, n: int) -> int:
3
4        prev1, prev2 = 1, 1
5        for i in range(2, n + 1):
6            curr = prev1 + prev2
7            prev2 = prev1
8            prev1 = curr
9
10        return prev1
11
12
13        
14        