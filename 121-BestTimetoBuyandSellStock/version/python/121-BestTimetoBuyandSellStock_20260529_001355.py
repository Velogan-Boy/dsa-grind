# Last updated: 5/29/2026, 12:13:55 AM
1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3
4        minPrice = float('inf')
5        maxProfit = float('-inf')
6        for price in prices:
7            if price < minPrice:
8                minPrice = price
9            
10            maxProfit = max(maxProfit, price - minPrice)
11
12        return maxProfit
13
14        