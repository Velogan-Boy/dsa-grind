# Climbing Stairs

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Easy
- **URL:** https://leetcode.com/problems/climbing-stairs/submissions/1977243514/
- **Date:** 2026-04-13

## Solution

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
        
        prev2 = 1
        prev1 = 1
        
        for i in range(2, n + 1):
            curr = prev1 + prev2
            prev2 = prev1
            prev1 = curr
        
        return prev1
```

---
*Generated automatically by LeetFeedback Extension*
