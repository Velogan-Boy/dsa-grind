# Best Time to Buy and Sell Stock II

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/submissions/1980252973/
- **Date:** 2026-04-16

## Solution

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        memo = [[-1] * 2 for _ in range(n)]

        def dfs(day, buy):
            if day == n: return 0

            if memo[day][buy] != -1: return memo[day][buy]

            if buy:
                memo[day][buy] = max(-prices[day] + dfs(day + 1, 0), dfs(day + 1, 1))
            else:
                memo[day][buy] = max(prices[day] + dfs(day + 1, 1), dfs(day + 1, 0))

            return memo[day][buy]


        return dfs(0, 1)



        
```

---
*Generated automatically by LeetFeedback Extension*
