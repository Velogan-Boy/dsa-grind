# Longest Substring Without Repeating Characters

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/2016617954/
- **Date:** 2026-05-29

## Solution

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j = 0, 0
        hashMap = {}
        ans = 0

        while j < len(s):
            if s[j] in hashMap:
                i = max(i, hashMap[s[j]] + 1)

            hashMap[s[j]] = j
            ans = max(ans, j - i + 1)
            j+=1

        return ans

            

        
```

---
*Generated automatically by LeetFeedback Extension*
