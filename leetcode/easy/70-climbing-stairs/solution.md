# Climbing Stairs

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Easy
- **URL:** https://leetcode.com/problems/climbing-stairs/submissions/2017520812/
- **Date:** 2026-05-30

## Solution

```python
class Solution:
    def climbStairs(self, n: int) -> int:

        prev1, prev2 = 1, 1
        for i in range(2, n + 1):
            curr = prev1 + prev2
            prev2 = prev1
            prev1 = curr

        return prev1


        
        
```

---
*Generated automatically by LeetFeedback Extension*
