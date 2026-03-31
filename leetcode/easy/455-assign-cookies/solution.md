# Assign Cookies

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Easy
- **URL:** https://leetcode.com/problems/assign-cookies/submissions/1964618140/
- **Date:** 2026-03-31

## Solution

```python
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        m = len(g)
        n = len(s)

        l,r = 0, 0

        while l < m and r < n:
            if g[l] <= s[r]:
                l+=1
            
            r+=1
            
        return l 


            
```

---
*Generated automatically by LeetFeedback Extension*
