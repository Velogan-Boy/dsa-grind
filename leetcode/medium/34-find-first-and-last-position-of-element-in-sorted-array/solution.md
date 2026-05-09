# Find First and Last Position of Element in Sorted Array

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/submissions/1998599113/
- **Date:** 2026-05-09

## Solution

```python
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        s = self.binarySearch(nums,target, True)
        e = self.binarySearch(nums,target, False)

        return [s, e]

    def binarySearch(self, nums: List[int], target: int, firstOccurence: bool) -> int:
        l, h = 0, len(nums)-1
        ans = -1

        while l <= h:
            mid = (l + h) // 2
            if nums[mid] > target: h = mid - 1
            elif nums[mid] < target: l = mid + 1
            else:
                ans = mid

                if firstOccurence: h = mid - 1
                else: l = mid + 1

                

        
        return ans


        
```

---
*Generated automatically by LeetFeedback Extension*
