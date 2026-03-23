# Remove K Digits

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/remove-k-digits/
- **Date:** 2026-03-23

## Solution

```python
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for i in num:
            while stack and stack[-1] > i and k > 0:
                k -= 1
                stack.pop()
            if stack or i is not "0":
                stack.append(i)
        if k:
            stack = stack[:-k]
        return ''.join(stack) or '0'
        

```

---
*Generated automatically by LeetFeedback Extension*
