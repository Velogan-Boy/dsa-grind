# Binary Search

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Easy
- **URL:** https://leetcode.com/problems/binary-search/submissions/1998582314/
- **Date:** 2026-05-09

## Solution

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l = 0
        r = len(nums) - 1

        while l <= r:
            mid =  ( l + r ) // 2

            if nums[mid] == target: return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return -1
        
```

---
*Generated automatically by LeetFeedback Extension*
