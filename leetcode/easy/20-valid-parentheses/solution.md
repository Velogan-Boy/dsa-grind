# Valid Parentheses

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Easy
- **URL:** https://leetcode.com/problems/valid-parentheses/submissions/2007381736/
- **Date:** 2026-05-19

## Solution

```python
class Solution:
    def isValid(self, s: str) -> bool:

        hashMap = {'}': '{', ')': '(', ']':'['}
        stack = []

        for ch in s:
            if stack and ch in hashMap and stack[-1] == hashMap[ch]:
                stack.pop()
            else:
                stack.append(ch)

        return not stack
            

        
```

---
*Generated automatically by LeetFeedback Extension*
