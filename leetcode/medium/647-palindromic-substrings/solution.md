# Palindromic Substrings

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/palindromic-substrings/submissions/2058119634/
- **Date:** 2026-07-06

## Solution

```python
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)

        ans = 0
        for i in range(n):
            ans += self.expandFromCenter(s,i, i)
            ans += self.expandFromCenter(s,i, i + 1)
        
        return ans




    def expandFromCenter(self, s, i, j):
        n = len(s)
        count = 0

        while i >= 0 and j < n and s[i] == s[j]:
            i-=1
            j+=1
            count += 1
        
        return count
        

        
```

---
*Generated automatically by LeetFeedback Extension*
