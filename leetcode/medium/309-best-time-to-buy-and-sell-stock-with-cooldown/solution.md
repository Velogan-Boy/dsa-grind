# Best Time to Buy and Sell Stock with Cooldown

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/submissions/1980289904/
- **Date:** 2026-04-16

## Solution

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        # 0 - cant buy
        # 1 - cant buy - cooldown
        # 2 - buy

        @cache
        def dfs(day, buy):
            if day == n: return 0

            if buy == 1:
                return dfs(day + 1, 2)
                
            elif buy == 2:
                return max(
                    -prices[day] + dfs(day + 1, 0),
                    dfs(day + 1, 2)
                )
            else:
                return max(
                    prices[day] + dfs(day + 1, 1),
                    dfs(day + 1, 0)
                )

        return dfs(0, 2)
```

---
*Generated automatically by LeetFeedback Extension*
