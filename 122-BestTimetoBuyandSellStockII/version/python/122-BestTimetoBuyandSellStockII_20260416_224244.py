# Last updated: 4/16/2026, 10:42:44 PM
1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        n = len(prices)
4
5        future = [0] * 2 
6
7        for day in range(n - 1, -1, -1):
8            curr = [0] * 2
9            curr[1] = max(-prices[day] + future[0], future[1])
10            curr[0] = max(prices[day] + future[1], future[0])
11            future = curr
12
13        return future[1]
14
15
16
17
18
19        