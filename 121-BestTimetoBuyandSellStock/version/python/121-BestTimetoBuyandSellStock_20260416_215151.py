# Last updated: 4/16/2026, 9:51:51 PM
1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        n = len(prices)
4
5        maxProfit = 0
6        minimum = prices[0]
7
8        for i in range(1, n):
9            profit = prices[i] - minimum
10            maxProfit = max(maxProfit, profit)
11
12            minimum = min(prices[i], minimum)
13
14        return maxProfit
15            
16
17
18        