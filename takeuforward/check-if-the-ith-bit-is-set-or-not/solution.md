# Check if the i-th bit is Set or Not

## Problem Information
- **Platform:** Takeuforward
- **Difficulty:** Unknown
- **URL:** https://takeuforward.org/plus/dsa/problems/check-if-the-i-th-bit-is-set-or-not
- **Date:** 2026-03-21

## Solution

```python
class Solution:
    def checkIthBit(self, n: int, i: int) -> bool:
        
        return n & (1 << i)

```

---
*Generated automatically by LeetFeedback Extension*
