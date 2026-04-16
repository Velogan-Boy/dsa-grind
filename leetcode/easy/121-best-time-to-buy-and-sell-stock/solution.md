# Best Time to Buy and Sell Stock

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Easy
- **URL:** https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/1980222287/
- **Date:** 2026-04-16

## Solution

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        maxProfit = 0
        minimum = prices[0]

        for i in range(1, n):
            profit = prices[i] - minimum
            maxProfit = max(maxProfit, profit)

            minimum = min(prices[i], minimum)

        return maxProfit
            


        
```

---
*Generated automatically by LeetFeedback Extension*
