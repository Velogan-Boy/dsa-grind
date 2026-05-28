# Best Time to Buy and Sell Stock

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Easy
- **URL:** https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/2015798842/
- **Date:** 2026-05-28

## Solution

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        minPrice = float('inf')
        maxProfit = float('-inf')
        for price in prices:
            if price < minPrice:
                minPrice = price
            
            maxProfit = max(maxProfit, price - minPrice)

        return maxProfit

        
```

---
*Generated automatically by LeetFeedback Extension*
