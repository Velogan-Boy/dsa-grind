# Move Zeroes

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Easy
- **URL:** https://leetcode.com/problems/move-zeroes/submissions/1994149749/
- **Date:** 2026-05-03

## Solution

```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        
        i = 0
        j = 0

        while j < len(nums):
            if nums[j] != 0:
                nums[i] = nums[j]
                i+=1
            
            j+=1

        while i < len(nums):
            nums[i] = 0
            i+=1
        
        
```

---
*Generated automatically by LeetFeedback Extension*
