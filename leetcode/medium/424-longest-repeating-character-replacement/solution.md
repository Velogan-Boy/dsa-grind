# Longest Repeating Character Replacement

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/longest-repeating-character-replacement/submissions/1960004178/
- **Date:** 2026-03-26

## Solution

```python
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        maxLength = 0
        l,r = 0, 0
        hm = {}
        maxF = 0

        while r < n:
            hm[s[r]] = hm.get(s[r], 0) + 1
            maxF = max(maxF, hm[s[r]])

            if r - l + 1 - maxF > k:
                hm[s[l]] = hm[s[l]] - 1
                maxF = max(maxF, hm[s[l]])
                l+=1
            
            maxLength = max(r - l + 1, maxLength)
            r+=1

        return maxLength





                


```

---
*Generated automatically by LeetFeedback Extension*
