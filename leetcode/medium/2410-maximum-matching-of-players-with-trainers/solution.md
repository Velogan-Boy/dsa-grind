# Maximum Matching of Players With Trainers

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/maximum-matching-of-players-with-trainers/submissions/1964619449/
- **Date:** 2026-03-31

## Solution

```python
class Solution:
    def matchPlayersAndTrainers(self, g: List[int], s: List[int]) -> int:

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
