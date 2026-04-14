# Coin Change II

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/coin-change-ii/submissions/1978108680/
- **Date:** 2026-04-14

## Solution

```python
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        memo = [[-1] * (amount + 1) for _ in range(n)]

        def dfs(i, a):
            if a == 0: return 1
            if i < 0: return 0
            if a < 0: return 0
            
            if memo[i][a] != -1: return memo[i][a]

            pick = dfs(i, a - coins[i])
            notPick = dfs(i - 1, a)

            memo[i][a] = pick + notPick

            return memo[i][a]


        return dfs(n - 1, amount)

       
```

---
*Generated automatically by LeetFeedback Extension*
