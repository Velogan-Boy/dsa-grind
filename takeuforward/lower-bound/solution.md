# Lower Bound

## Problem Information
- **Platform:** Takeuforward
- **Difficulty:** Unknown
- **URL:** https://takeuforward.org/plus/dsa/problems/lower-bound-
- **Date:** 2026-05-09

## Solution

```python
class Solution:
    def lowerBound(self, nums, x):
        n = len(nums)
        l, r = 0, n - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] >= x:
                r = mid - 1
            else:
                l = mid + 1
        
        return l
       



```

---
*Generated automatically by LeetFeedback Extension*
