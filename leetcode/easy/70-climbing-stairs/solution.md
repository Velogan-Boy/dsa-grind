# Climbing Stairs

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Easy
- **URL:** https://leetcode.com/problems/climbing-stairs/
- **Date:** 2026-05-30

## Solution

```python
class Solution:
    def climbStairs(self, n: int) -> int:


        for i in range(2, n + 1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]


        
        
```

---
*Generated automatically by LeetFeedback Extension*
