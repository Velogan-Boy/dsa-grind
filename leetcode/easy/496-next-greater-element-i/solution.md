# Next Greater Element I

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Easy
- **URL:** https://leetcode.com/problems/next-greater-element-i/submissions/2051530583/
- **Date:** 2026-06-30

## Solution

```python
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        stack = []
        nextGreater = {}

        for i in range(len(nums2) - 1, -1, -1):

            while stack and stack[-1] <= nums2[i]:
                stack.pop()

            nextGreater[nums2[i]] = stack[-1] if stack else -1

            stack.append(nums2[i])

        ans = []

        for num in nums1:
            ans.append(nextGreater[num])

        return ans
```

---
*Generated automatically by LeetFeedback Extension*
