# Last updated: 4/16/2026, 11:02:52 PM
1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        n = len(prices)
4
5        # 0 - cant buy
6        # 1 - cant buy - cooldown
7        # 2 - buy
8
9        @cache
10        def dfs(day, buy):
11            if day == n: return 0
12
13            if buy == 1:
14                return dfs(day + 1, 2)
15                
16            elif buy == 2:
17                return max(
18                    -prices[day] + dfs(day + 1, 0),
19                    dfs(day + 1, 2)
20                )
21            else:
22                return max(
23                    prices[day] + dfs(day + 1, 1),
24                    dfs(day + 1, 0)
25                )
26
27        return dfs(0, 2)