# Product of Array Except Self

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/product-of-array-except-self/submissions/2021579476/
- **Date:** 2026-06-03

## Solution

```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n

        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i-1]
        
        for i in range(n - 2 , -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]

        ans = [1] * n

        for i in range(n):
            ans[i] = prefix[i] * suffix[i]

        return ans


        
        




        
```

---
*Generated automatically by LeetFeedback Extension*
