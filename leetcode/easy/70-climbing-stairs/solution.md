# Climbing Stairs

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Easy
- **URL:** https://leetcode.com/problems/climbing-stairs/submissions/2017518119/
- **Date:** 2026-05-30

## Solution

```python
class Solution:
    def climbStairs(self, n: int) -> int:

        @cache
        def dfs(n):
            if n == 0 or n == 1: return 1

            return dfs(n - 1) + dfs(n - 2)

        return dfs(n)

        
        
```

---
*Generated automatically by LeetFeedback Extension*
