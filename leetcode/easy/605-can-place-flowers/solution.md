# Can Place Flowers

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Easy
- **URL:** https://leetcode.com/problems/can-place-flowers/submissions/1990431738/
- **Date:** 2026-04-28

## Solution

```python
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        empty = 0
        f = [0] + flowerbed + [0]

        for i in range(1, len(f) - 1):
            if f[i] == 1: continue

            if f[i - 1] == 0 and f[i + 1] == 0:
                empty+=1
                f[i] = 1

        return empty >= n
        


        
```

---
*Generated automatically by LeetFeedback Extension*
