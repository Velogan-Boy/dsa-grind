# Longest Substring Without Repeating Characters

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/2016630538/
- **Date:** 2026-05-29

## Solution

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j = 0, 0
        n = len(s)
        hashMap = {}
        ans = 0

        while j < n:
            if s[j] in hashMap:
                i = max(hashMap[s[j]] + 1, i)
            
            hashMap[s[j]] = j
            ans = max(ans, j - i + 1)
            j+=1

        return ans

            


        
```

---
*Generated automatically by LeetFeedback Extension*
