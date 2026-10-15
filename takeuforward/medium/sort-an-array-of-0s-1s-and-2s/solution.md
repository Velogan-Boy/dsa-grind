# Sort an array of 0's 1's and 2's

## Problem Information
- **Platform:** Takeuforward
- **Difficulty:** Medium
- **URL:** https://takeuforward.org/practice/dsa/sort-an-array-of-0's-1's-and-2's
- **Date:** 2026-10-15

## Solution

```python
class Solution:
    def sortZeroOneTwo(self, nums):
        n = len(nums)

        i, j, k = 0, 0, n - 1

        while j <= k:
            if nums[j] == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1

            elif nums[j] == 2:
                nums[k], nums[j] = nums[j], nums[k]
                k -= 1

            else:  
                j += 1

        return nums
```

---
*Generated automatically by LeetFeedback Extension*
