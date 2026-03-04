# Largest Element

## Problem Information
- **Platform:** Takeuforward
- **Difficulty:** Unknown
- **URL:** https://takeuforward.org/plus/dsa/problems/largest-element
- **Date:** 2026-03-04

## Solution

```python
from typing import List

class Solution:
    def largestElement(self, nums):
        nums.sort()

        largest = nums[-1]

        return largest



```

---
*Generated automatically by LeetFeedback Extension*
