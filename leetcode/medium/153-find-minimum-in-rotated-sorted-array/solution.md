# Find Minimum in Rotated Sorted Array

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/submissions/1998642594/
- **Date:** 2026-05-09

## Solution

```python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        s = 0
        e = len(nums) - 1
        ans = inf

        while s <= e:
            mid = (s + e) // 2

            if nums[s] <= nums[mid]:
                ans = min(ans,nums[s])
                s = mid + 1
            else:
                ans = min(ans,nums[mid])
                e = mid - 1
        
        return ans if ans != inf else -1


        
```

---
*Generated automatically by LeetFeedback Extension*
