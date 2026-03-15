# Last updated: 3/15/2026, 6:51:27 PM
1class Solution:
2    def myPow(self, x: float, n: int) -> float:
3
4        def helper(x, n):
5            if n == 0:
6                return 1
7
8            half = helper(x, n // 2)
9
10            if n % 2 == 0:
11                return half * half
12            else:
13                return half * half * x
14
15        if n < 0:
16            x = 1 / x
17            n = -n
18
19        return helper(x, n)