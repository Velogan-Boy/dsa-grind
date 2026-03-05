# Koko Eating Bananas

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/koko-eating-bananas/submissions/1938754335/
- **Date:** 2026-03-05

## Solution

```python
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        totalBananas = sum(piles)
        if not totalBananas: return 0

        s = 1
        e = max(piles)

        while s <= e:
            k = (s + e) // 2

            hour = 0
            for i in range(len(piles)):
                hour += math.ceil(piles[i] / k)
            
            if hour <= h: 
                e = k - 1
            else: s = k + 1
    
           
        return s
```

---
*Generated automatically by LeetFeedback Extension*
