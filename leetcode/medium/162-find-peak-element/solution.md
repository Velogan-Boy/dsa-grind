# Find Peak Element

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/find-peak-element/
- **Date:** 2026-05-09

## Solution

```python
class Solution:
    def findPeakElement(self, nums):
        n = len(nums)
        low, high = 0, n - 1

        while low < high:
            mid = (low + high) // 2

            if nums[mid] > nums[mid + 1]:
                high = mid
            else:
                low = mid + 1

        return low
```

---
*Generated automatically by LeetFeedback Extension*
