# Zigzag Conversion

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/zigzag-conversion/submissions/1989497916/
- **Date:** 2026-04-27

## Solution

```python
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        rows = [""] * numRows
        curr_row = 0
        direction = 1  # 1 = down, -1 = up

        for ch in s:
            rows[curr_row] += ch

            if curr_row == 0:
                direction = 1
            elif curr_row == numRows - 1:
                direction = -1

            curr_row += direction

        return "".join(rows)
```

---
*Generated automatically by LeetFeedback Extension*
