# Valid Parentheses

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Easy
- **URL:** https://leetcode.com/problems/valid-parentheses/submissions/1956059068/
- **Date:** 2026-03-22

## Solution

```python
class Solution:
    def isValid(self, s: str) -> bool:
        bracketMap = {")": "(", "]": "[", "}": "{"}
        stack = []

        for c in s:
            if c not in bracketMap:
                stack.append(c)
                continue

            if not stack or stack[-1] != bracketMap[c]:
                return False
                
            stack.pop()

        return not stack

```

---
*Generated automatically by LeetFeedback Extension*
