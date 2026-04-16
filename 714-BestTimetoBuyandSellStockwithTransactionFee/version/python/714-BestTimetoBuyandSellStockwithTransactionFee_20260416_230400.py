# Last updated: 4/16/2026, 11:04:00 PM
1class Solution:
2    def maxProfit(self, prices: List[int],fee:int) -> int:
3        
4        dp = [[-1,-1] for _ in range(len(prices))]
5
6        return self.recRun(prices,0, 1,dp,fee)
7
8    def recRun(self, prices, i , buy,dp,fee):
9
10        if i == len(prices):
11            return 0
12
13        if dp[i][buy] != -1:
14            return dp[i][buy]
15        
16        if buy == 1:
17            dp[i][buy] = max(
18                -prices[i] + self.recRun(prices,i + 1, 0,dp,fee),
19                self.recRun(prices,i + 1, 1,dp,fee)
20            )
21        
22        else:
23            dp[i][buy] = max(
24                +prices[i] - fee + self.recRun(prices,i + 1, 1,dp,fee),
25                self.recRun(prices,i + 1, 0,dp,fee)
26            )
27        
28        return dp[i][buy]
29
30        
31        