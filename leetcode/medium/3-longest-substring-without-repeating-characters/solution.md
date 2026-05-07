# Longest Substring Without Repeating Characters

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/1997454398/
- **Date:** 2026-05-07

## Solution

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j = 0, 0
        hashSet = set()
        ans = 0

        while j < len(s):
            if s[j] in hashSet:
                hashSet.remove(s[i])
                i+=1
            else:
                hashSet.add(s[j])
                ans = max(ans, j - i + 1)
                j+=1

            

        return ans

            

        
```

---
*Generated automatically by LeetFeedback Extension*
