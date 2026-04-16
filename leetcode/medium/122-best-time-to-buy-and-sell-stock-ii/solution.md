# Best Time to Buy and Sell Stock II

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/submissions/1980268654/
- **Date:** 2026-04-16

## Solution

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        dp = [[-1] * 2 for _ in range(n + 1)]

        dp[n][1] = dp[n][0] = 0

        for day in range(n - 1, -1, -1):
            dp[day][1] = max(-prices[day] + dp[day + 1][0], dp[day + 1][1])
            dp[day][0] = max(prices[day] + dp[day + 1][1], dp[day + 1][0])

        return dp[0][1]





        
```

---
*Generated automatically by LeetFeedback Extension*
