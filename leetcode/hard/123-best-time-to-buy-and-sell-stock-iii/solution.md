# Best Time to Buy and Sell Stock III

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Hard
- **URL:** https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/submissions/1980277488/
- **Date:** 2026-04-16

## Solution

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        
        @cache  
        def dfs(day, buy, cap):
            if day == n: return 0
            if cap == 0: return 0

            if buy:
                return max( -prices[day] + dfs(day + 1, 0, cap), dfs(day + 1, 1, cap))
            else:
                return max( prices[day] + dfs(day + 1, 1, cap - 1), dfs(day + 1, 0 , cap))

        return dfs(0, 1, 2)


```

---
*Generated automatically by LeetFeedback Extension*
