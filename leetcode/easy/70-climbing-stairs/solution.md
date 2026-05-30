# Climbing Stairs

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Easy
- **URL:** https://leetcode.com/problems/climbing-stairs/submissions/2017518728/
- **Date:** 2026-05-30

## Solution

```python
class Solution:
    def climbStairs(self, n: int) -> int:

        dp = [-1] * (n + 1)

        def dfs(n):
            if n == 0 or n == 1: return 1

            if dp[n] != -1: return dp[n]

            dp[n] = dfs(n - 1) + dfs(n - 2)

            return dp[n]

        return dfs(n)

        
        
```

---
*Generated automatically by LeetFeedback Extension*
