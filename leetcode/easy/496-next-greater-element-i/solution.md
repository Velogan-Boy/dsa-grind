# Next Greater Element I

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Easy
- **URL:** https://leetcode.com/problems/next-greater-element-i/submissions/1956598451/
- **Date:** 2026-03-23

## Solution

```python
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        n = len(nums2)
        stack = []
        ans = [-1] * n
        hashMap = {}

        for i in range(n - 1, -1, -1):
            hashMap[nums2[i]] = i

            while stack and stack[-1] <= nums2[i]:
                stack.pop()

            if stack:
                ans[i] = stack[-1]
            
            stack.append(nums2[i])

        res = []
        for num in nums1:
            res.append(ans[hashMap[num]])

        return res



     
```

---
*Generated automatically by LeetFeedback Extension*
