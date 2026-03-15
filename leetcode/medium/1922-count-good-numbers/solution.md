# Count Good Numbers

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/count-good-numbers/submissions/1949134393/
- **Date:** 2026-03-15

## Solution

```python
class Solution:
    def countGoodNumbers(self, n: int) -> int:

        def myPow(x, n, mod):
            result = 1
            x = x % mod

            while n > 0:
                if n % 2 == 1:
                    result = (result * x) % mod
                x = (x * x) % mod
                n //= 2

            return result

        
        MODULO = 10**9 + 7

        return ( myPow(5, math.ceil(n / 2),MODULO) * myPow(4, n // 2,MODULO) ) % MODULO
        
```

---
*Generated automatically by LeetFeedback Extension*
