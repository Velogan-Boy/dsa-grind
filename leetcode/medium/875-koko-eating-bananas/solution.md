# Koko Eating Bananas

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/koko-eating-bananas/submissions/1998735985/
- **Date:** 2026-05-09

## Solution

```python
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)

        def reqHours(k):
            hoursTaken = 0
            for pile in piles:
                hoursTaken += ceil(pile/k)

            return hoursTaken
            

        while low <= high:
            k = (low + high) // 2

            if reqHours(k) <= h:
                high = k - 1
            else:
                low = k + 1
        
        return low






        
```

---
*Generated automatically by LeetFeedback Extension*
