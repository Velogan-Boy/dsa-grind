# Longest Substring Without Repeating Characters

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/2074908568/
- **Date:** 2026-07-20

## Solution

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hm = {}
        i = 0
        ans = 0

        for j in range(len(s)):
            if s[j] in hm:
                i = max(i, hm[s[j]] + 1)

            hm[s[j]] = j
            ans = max(ans, j - i + 1)

        return ans
```

---
*Generated automatically by LeetFeedback Extension*
