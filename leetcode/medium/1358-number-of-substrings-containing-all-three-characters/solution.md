# Number of Substrings Containing All Three Characters

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/
- **Date:** 2026-03-28

## Solution

```python
class Solution:
    def numberOfSubstrings(self, s: str) -> int:

        n = len(s)
        lastSeen = [-1, -1, -1]
        count = 0
        j = 0

        for i in range(n):
            lastSeen[ord(s[i]) - ord('a')] = i
            count += 1 + min(lastSeen[0], lastSeen[1], lastSeen[2])
    
        return count



        
```

---
*Generated automatically by LeetFeedback Extension*
