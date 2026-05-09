# Search in Rotated Sorted Array II

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/search-in-rotated-sorted-array-ii/submissions/1998637619/
- **Date:** 2026-05-09

## Solution

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        s = 0
        e = len(nums) - 1

        while s <= e:
            mid =  (s + e) // 2

            if nums[mid] == target: return True

            if nums[mid] == nums[s] and nums[mid] == nums[e]:
                s += 1
                e -= 1
                continue

            if nums[s] <= nums[mid]:
                if nums[s] <= target and target <= nums[mid]:
                    e = mid - 1
                else:
                    s = mid + 1
            else:
                if nums[mid] <= target and target <= nums[e]:
                    s = mid + 1
                else:
                    e = mid - 1
            
        return False



```

---
*Generated automatically by LeetFeedback Extension*
