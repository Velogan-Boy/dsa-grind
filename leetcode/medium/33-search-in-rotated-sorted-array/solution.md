# Search in Rotated Sorted Array

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/search-in-rotated-sorted-array/
- **Date:** 2026-05-09

## Solution

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        n = len(nums)
        s, e = 0, n - 1

        while s <= e:
            mid = (s + e) // 2

            if nums[mid] == target: return mid

            if nums[s] <= nums[mid]:
                if nums[s] <= target <= nums[mid]:
                    e = mid - 1
                else:
                    s = mid + 1
            else:
                if nums[mid] <= target <= nums[e]:
                    s = mid + 1
                else:
                    e = mid - 1
        
        return -1
                
                


     


```

---
*Generated automatically by LeetFeedback Extension*
