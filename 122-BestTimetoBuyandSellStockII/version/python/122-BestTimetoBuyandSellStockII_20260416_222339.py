# Last updated: 4/16/2026, 10:23:39 PM
1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        n = len(prices)
4
5        memo = [[-1] * 2 for _ in range(n)]
6
7        def dfs(day, buy):
8            if day == n: return 0
9
10            if memo[day][buy] != -1: return memo[day][buy]
11
12            if buy:
13                memo[day][buy] = max(-prices[day] + dfs(day + 1, 0), dfs(day + 1, 1))
14            else:
15                memo[day][buy] = max(prices[day] + dfs(day + 1, 1), dfs(day + 1, 0))
16
17            return memo[day][buy]
18
19
20        return dfs(0, 1)
21
22
23
24        