# Kids With the Greatest Number of Candies

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Easy
- **URL:** https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
- **Date:** 2026-04-28

## Solution

```python
class Solution:
    def kidsWithCandies(self, candies, extraCandies):

        result = []
        maxVal = max(candies)

        for c in candies:
            result.append(c + extraCandies >= maxVal)

        return result
```

---
*Generated automatically by LeetFeedback Extension*
