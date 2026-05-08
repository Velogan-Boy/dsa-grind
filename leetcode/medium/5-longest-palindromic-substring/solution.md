# Longest Palindromic Substring

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/longest-palindromic-substring/submissions/1998299486/
- **Date:** 2026-05-08

## Solution

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        if n <= 1: return s

        def expandFromCenter(l, r):
            while l >= 0 and r < n and s[l] == s[r]:
                l-=1
                r+=1
            
            return s[l+1:r]

        maxP = s[0]
        for i in range(n):
            odd = expandFromCenter(i,i)
            even = expandFromCenter(i, i + 1)

            if len(odd) > len(maxP):
                maxP = odd
            
            if len(even) > len(maxP):
                maxP = even
            
        return maxP
        



       
```

---
*Generated automatically by LeetFeedback Extension*
