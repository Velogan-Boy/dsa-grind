# Last updated: 4/16/2026, 10:50:10 PM
1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        n = len(prices)
4        
5        @cache  
6        def dfs(day, buy, cap):
7            if day == n: return 0
8            if cap == 0: return 0
9
10            if buy:
11                return max( -prices[day] + dfs(day + 1, 0, cap), dfs(day + 1, 1, cap))
12            else:
13                return max( prices[day] + dfs(day + 1, 1, cap - 1), dfs(day + 1, 0 , cap))
14
15        return dfs(0, 1, 2)
16
17