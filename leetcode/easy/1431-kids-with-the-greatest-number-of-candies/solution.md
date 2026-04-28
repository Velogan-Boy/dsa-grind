# Kids With the Greatest Number of Candies

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Easy
- **URL:** https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/submissions/1990412340/
- **Date:** 2026-04-28

## Solution

```python
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        maxCandy = max(candies)
        res = [False] * len(candies)

        for i, candy in enumerate(candies):
            if candy + extraCandies >= maxCandy:
                res[i] = True
        
        return res
        
```

---
*Generated automatically by LeetFeedback Extension*
