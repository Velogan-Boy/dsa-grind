# Maximum Product Subarray in an Array

## Problem Information
- **Platform:** Takeuforward
- **Difficulty:** Medium
- **URL:** https://takeuforward.org/practice/dsa/maximum-product-subarray-in-an-array
- **Date:** 2026-10-14

## Solution

```python
class Solution:
    def maxProduct(self, nums):

        curr_max = nums[0]
        curr_min = nums[0]
        result = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]

            if num < 0:
                curr_max, curr_min = curr_min, curr_max

            curr_max = max(num, curr_max * num)
            curr_min = min(num, curr_min * num)

            result = max(result, curr_max)

        return result


            
        
```

---
*Generated automatically by LeetFeedback Extension*
