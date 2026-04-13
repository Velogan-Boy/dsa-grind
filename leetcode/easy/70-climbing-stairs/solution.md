# Climbing Stairs

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Easy
- **URL:** https://leetcode.com/problems/climbing-stairs/description/
- **Date:** 2026-04-13

## Solution

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1] * (n + 1)

        def dfs(n):
            if n < 0:
                return 0

            if n == 0 or n == 1:
                return 1
            
            if dp[n] != -1:
                return dp[n]
            
            dp[n] = dfs(n - 1) + dfs(n - 2)
            return dp[n]
        
        return dfs(n)
```

---
*Generated automatically by LeetFeedback Extension*
