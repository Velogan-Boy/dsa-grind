# Next Greater Element II

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/next-greater-element-ii/submissions/2052651108/
- **Date:** 2026-07-01

## Solution

```python
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nge = [-1] * n
        stack = []

        for i in range(n*2-1, -1, -1):
            while stack and stack[-1] <= nums[i % n]:
                stack.pop()
            
            if i < n:
                nge[i] = stack[-1] if stack else -1
            
            stack.append(nums[i % n])

        return nge

        

        
```

---
*Generated automatically by LeetFeedback Extension*
