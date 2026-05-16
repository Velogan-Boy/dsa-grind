# Last updated: 5/17/2026, 12:45:01 AM
1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        n = len(prices)
4        dp = [[-1] * 2 for _ in range(n)]
5        # max(dfs(i + 1, 1), dfs(i + 1, 0))
6
7        # max profit till ith day
8        def dfs(i, curr):
9            # curr = 0 -> i cannot buy
10            # curr = 1 -> i can buy
11            if i == n: return 0
12
13            if dp[i][curr] != -1: return dp[i][curr]
14
15            buy = float('-inf')
16            dontBuy = float('-inf')
17            hold = float('-inf')
18            sell = float('-inf')
19
20            if curr == 1: 
21                buy = dfs(i + 1, 0) - prices[i]
22                dontBuy = dfs(i + 1, 1)
23            else:
24                hold = dfs(i + 1, 0)
25                sell = dfs(i + 1, 1) + prices[i]
26            
27            dp[i][curr] = max(buy, hold, sell, dontBuy)
28            return dp[i][curr]
29
30        return dfs(0, 1)
31        