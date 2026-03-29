# Minimum Window Substring

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Hard
- **URL:** https://leetcode.com/problems/minimum-window-substring/
- **Date:** 2026-03-29

## Solution

```python
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)

        hm = [0] * 256
        for c in t:
            hm[ord(c)] += 1

        l = 0
        count = 0
        minLength = inf
        start = -1

        for r in range(n):
            if hm[ord(s[r])] > 0:
                count += 1
            
            hm[ord(s[r])] -= 1

            while count == len(t):
                if r - l + 1 < minLength:
                    minLength = r - l + 1
                    start = l
                
                hm[ord(s[l])] += 1
                if hm[ord(s[l])] > 0:
                    count -= 1
                
                l += 1

        return "" if start == -1 else s[start:start + minLength]
```

---
*Generated automatically by LeetFeedback Extension*
