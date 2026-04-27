# Zigzag Conversion

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/zigzag-conversion/submissions/1989495311/
- **Date:** 2026-04-27

## Solution

```python
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        res = ""
        n = len(s)
        increment = 2 * (numRows - 1)

        for row in range(numRows):
            for i in range(row, n, increment):
                res += s[i]

                if row != 0 and row != numRows - 1:
                    diag = i + increment - 2 * row
                    if diag < n:
                        res += s[diag]

        return res
```

---
*Generated automatically by LeetFeedback Extension*
