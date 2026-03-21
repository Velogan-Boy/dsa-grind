# Count the Number of Set Bits

## Problem Information
- **Platform:** Takeuforward
- **Difficulty:** Unknown
- **URL:** https://takeuforward.org/plus/dsa/problems/count-the-number-of-set-bits
- **Date:** 2026-03-21

## Solution

```python
class Solution:
    def countSetBits(self, n: int) -> int:
        
        cnt = 0
        while n != 0:
            n = n & (n - 1)
            cnt+=1

        return cnt
```

---
*Generated automatically by LeetFeedback Extension*
