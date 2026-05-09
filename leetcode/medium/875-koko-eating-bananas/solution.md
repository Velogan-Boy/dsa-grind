# Koko Eating Bananas

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/koko-eating-bananas/submissions/1998735151/
- **Date:** 2026-05-09

## Solution

```python
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()

        low = 1
        high = piles[-1]

        def reqHours(k):
            hoursTaken = 0
            for pile in piles:
                hoursTaken += ceil(pile/k)

            return hoursTaken
            

        while low <= high:
            mid = (low + high) // 2

            if reqHours(mid) <= h:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return ans






        
```

---
*Generated automatically by LeetFeedback Extension*
