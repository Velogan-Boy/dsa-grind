# Last updated: 4/13/2026, 4:36:51 PM
1class Solution:
2    def climbStairs(self, n: int) -> int:
3        if n <= 1:
4            return 1
5        
6        prev2 = 1
7        prev1 = 1
8        
9        for i in range(2, n + 1):
10            curr = prev1 + prev2
11            prev2 = prev1
12            prev1 = curr
13        
14        return prev1