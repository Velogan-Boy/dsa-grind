# Armstrong Number

## Problem Information
- **Platform:** Takeuforward
- **Difficulty:** Unknown
- **URL:** https://takeuforward.org/plus/dsa/problems/armstrong-number
- **Date:** 2026-07-29

## Solution

```python
class Solution:
    def isArmstrong(self, N: int) -> bool:
        
        req = 0
        num = N
        k = len(str(N))

        while num != 0:
            digit = num % 10
            num //= 10
            req += digit ** k
        
        return req == N



        
```

---
*Generated automatically by LeetFeedback Extension*
