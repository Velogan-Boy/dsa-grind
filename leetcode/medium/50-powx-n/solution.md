# Pow(x, n)

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/powx-n/submissions/1949109794/
- **Date:** 2026-03-15

## Solution

```python
class Solution:
    def myPow(self, x: float, n: int) -> float:

        def helper(x, n):
            if n == 0:
                return 1

            half = helper(x, n // 2)

            if n % 2 == 0:
                return half * half
            else:
                return half * half * x

        if n < 0:
            x = 1 / x
            n = -n

        return helper(x, n)
```

---
*Generated automatically by LeetFeedback Extension*
