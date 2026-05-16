# Last updated: 5/17/2026, 12:43:08 AM
1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        n = len(prices)
4        # max(dfs(i + 1, 1), dfs(i + 1, 0))
5
6        # max profit till ith day
7        @cache
8        def dfs(i, curr):
9            # curr = 0 -> i cannot buy
10            # curr = 1 -> i can buy
11            if i == n: return 0
12
13            buy = float('-inf')
14            dontBuy = float('-inf')
15            hold = float('-inf')
16            sell = float('-inf')
17
18            if curr == 1: 
19                buy = dfs(i + 1, 0) - prices[i]
20                dontBuy = dfs(i + 1, 1)
21            else:
22                hold = dfs(i + 1, 0)
23                sell = dfs(i + 1, 1) + prices[i]
24            
25            return max(buy, hold, sell, dontBuy)
26
27        return dfs(0, 1)
28        