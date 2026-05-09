# Search Insert Position

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Easy
- **URL:** https://leetcode.com/problems/search-insert-position/submissions/1998590941/
- **Date:** 2026-05-09

## Solution

```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        n = len(nums)
        l , r = 0, n - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] >= target:
                r = mid - 1
            else:
                l = mid + 1
        
        return l

        
```

---
*Generated automatically by LeetFeedback Extension*
