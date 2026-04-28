# Reverse Vowels of a String

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Easy
- **URL:** https://leetcode.com/problems/reverse-vowels-of-a-string/submissions/1990454385/
- **Date:** 2026-04-28

## Solution

```python
class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        i, j = 0, len(s) - 1

        while i < j:
            if s[i] not in 'aeiouAEIOU':
                i += 1
            elif s[j] not in 'aeiouAEIOU':
                j -= 1
            else:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
        
        return ''.join(s) 
```

---
*Generated automatically by LeetFeedback Extension*
