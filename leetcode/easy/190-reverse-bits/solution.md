# Reverse Bits

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Easy
- **URL:** https://leetcode.com/problems/reverse-bits/submissions/2009702053/
- **Date:** 2026-05-22

## Solution

```python
class Solution:
    def reverseBits(self, n: int) -> int:

        res = 0

        for i in range(32):
            bit = (n >> i) & 1
            res = res | (bit << (31 - i))

        return res

       
        
```

---
*Generated automatically by LeetFeedback Extension*
