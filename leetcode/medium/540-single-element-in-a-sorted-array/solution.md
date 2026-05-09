# Single Element in a Sorted Array

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/single-element-in-a-sorted-array/submissions/1998659563/
- **Date:** 2026-05-09

## Solution

```python
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        low, high = 0, n - 1

        while low <= high:
            mid = (low + high) // 2

            left_same = (mid > 0 and nums[mid] == nums[mid - 1])
            right_same = (mid < n - 1 and nums[mid] == nums[mid + 1])

            if not left_same and not right_same:
                return nums[mid]

            if (mid % 2 == 1 and left_same) or (mid % 2 == 0 and right_same):
                low = mid + 1
            else:
                high = mid - 1

        return -1


```

---
*Generated automatically by LeetFeedback Extension*
