# Minimum Bit Flips to Convert Number

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Easy
- **URL:** https://leetcode.com/problems/minimum-bit-flips-to-convert-number/submissions/1955564922/
- **Date:** 2026-03-22

## Solution

```python
class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:

        n = start ^ goal

        cnt = 0
        while n != 0:
            n = n & (n - 1)
            cnt += 1

        return cnt

        
```

---
*Generated automatically by LeetFeedback Extension*
