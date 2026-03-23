# Next Greater Element II

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/next-greater-element-ii/submissions/1956611442/
- **Date:** 2026-03-23

## Solution

```python
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:

        n = len(nums)
        stack = []
        ans = [-1] * n

        for i in range(2*n-1, -1, -1):
            while stack and stack[-1] <= nums[i % n]:
                stack.pop()
            
            if i < n:
                ans[i] = stack[-1] if stack else -1
            
            stack.append(nums[i % n])

        return ans

        

        
```

---
*Generated automatically by LeetFeedback Extension*
