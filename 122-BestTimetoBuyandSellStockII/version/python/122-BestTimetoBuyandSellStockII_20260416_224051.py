# Last updated: 4/16/2026, 10:40:51 PM
1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        n = len(prices)
4
5        dp = [[-1] * 2 for _ in range(n + 1)]
6
7        dp[n][1] = dp[n][0] = 0
8
9        for day in range(n - 1, -1, -1):
10            dp[day][1] = max(-prices[day] + dp[day + 1][0], dp[day + 1][1])
11            dp[day][0] = max(prices[day] + dp[day + 1][1], dp[day + 1][0])
12
13        return dp[0][1]
14
15
16
17
18
19        