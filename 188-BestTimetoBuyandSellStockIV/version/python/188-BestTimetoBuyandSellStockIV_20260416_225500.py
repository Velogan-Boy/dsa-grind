# Last updated: 4/16/2026, 10:55:00 PM
1class Solution:
2    def maxProfit(self, k, prices):
3        n = len(prices)
4
5        @cache
6        def dfs(day, buy, cap):
7            if day == n or cap == 0:
8                return 0
9
10            if buy:
11                return max(
12                    -prices[day] + dfs(day + 1, 0, cap),   
13                    dfs(day + 1, 1, cap)
14                )
15            else:
16                return max(
17                    prices[day] + dfs(day + 1, 1, cap - 1),  
18                    dfs(day + 1, 0, cap)
19                )
20
21        return dfs(0, 1, k)