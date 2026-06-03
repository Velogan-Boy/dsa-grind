# Product of Array Except Self

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/product-of-array-except-self/submissions/2021583981/
- **Date:** 2026-06-03

## Solution

```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        ans = [1] * n

        for i in range(1, n):
            ans[i] = ans[i - 1] * nums[i - 1]
        
        suffix = nums[n - 1]
        for i in range(n - 2 , -1, -1):
            ans[i] *= suffix
            suffix *= nums[i]

        return ans


        
        




        
```

---
*Generated automatically by LeetFeedback Extension*
