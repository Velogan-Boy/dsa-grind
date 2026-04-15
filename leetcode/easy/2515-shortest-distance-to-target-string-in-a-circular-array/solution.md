# Shortest Distance to Target String in a Circular Array

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Easy
- **URL:** https://leetcode.com/problems/shortest-distance-to-target-string-in-a-circular-array/submissions/1979320773/
- **Date:** 2026-04-15

## Solution

```python
class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        if words[startIndex] == target: return 0
        n = len(words)

        i, j = startIndex + 1, startIndex - 1

        d = 0

        for _ in range(n):
            i%=n
            j%=n
            d+=1

            if words[i] == target or words[j] == target: return d

            i+=1
            j-=1

        return -1
        
```

---
*Generated automatically by LeetFeedback Extension*
