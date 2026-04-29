# Product of Array Except Self

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/product-of-array-except-self/submissions/1991265025/
- **Date:** 2026-04-29

## Solution

```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = math.prod(nums)
        result = []
        if product == 1:
            return nums
        elif product != 0:
            for i in range(len(nums)):
                result.append(product//nums[i])
            return result
        else:
            for i in range(len(nums)):
                result.append(math.prod(nums[:i]+nums[i+1:]))
            return result
```

---
*Generated automatically by LeetFeedback Extension*
