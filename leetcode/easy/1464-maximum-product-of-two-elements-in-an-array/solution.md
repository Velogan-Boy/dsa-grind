# Maximum Product of Two Elements in an Array

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Easy
- **URL:** https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/submissions/2083487865/
- **Date:** 2026-07-27

## Solution

```python
class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        n = len(nums)
        maxValue = 0

        for i in range(n):
            for j in range(i + 1, n):
                currProd = (nums[i] - 1) * (nums[j] - 1)
                maxValue = max(currProd, maxValue)
            
        return maxValue

        
```

---
*Generated automatically by LeetFeedback Extension*
