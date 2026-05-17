# Maximum Product Subarray

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/maximum-product-subarray/
- **Date:** 2026-05-17

## Solution

```python
class Solution:
    def maxProduct(self, nums):
        ans = nums[0]
        maxProd = nums[0]
        minProd = nums[0]

        for i in range(1, len(nums)):
            curr = nums[i]

            if curr < 0:
                maxProd, minProd = minProd, maxProd

            maxProd = max(curr, maxProd * curr)
            minProd = min(curr, minProd * curr)

            ans = max(ans, maxProd)

        return ans
```

---
*Generated automatically by LeetFeedback Extension*
