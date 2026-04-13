# Minimum Distance to the Target Element

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Easy
- **URL:** https://leetcode.com/problems/minimum-distance-to-the-target-element/submissions/1977629634/
- **Date:** 2026-04-13

## Solution

```python
class Solution:
    def getMinDistance(self, nums: list[int], target: int, start: int) -> int:

        if nums[start] == target:
            return 0

        n = len(nums)
        d = 1

        while True:
            if start - d >= 0 and nums[start - d] == target:
                return d

            if start + d < n and nums[start + d] == target:
                return d

            d += 1
```

---
*Generated automatically by LeetFeedback Extension*
