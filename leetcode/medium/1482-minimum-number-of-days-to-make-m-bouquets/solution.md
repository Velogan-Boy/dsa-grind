# Minimum Number of Days to Make m Bouquets

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/submissions/1938795378/
- **Date:** 2026-03-05

## Solution

```python
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < k * m:
            return -1

        s = min(bloomDay)
        e = max(bloomDay)

        while s <= e:
            x = (s + e) // 2

            cnt = 0
            boquet = 0
            for i in range(len(bloomDay)):
                if bloomDay[i] <= x:
                    cnt += 1
                else:
                    boquet += cnt // k
                    cnt = 0

            boquet += cnt // k

            if boquet >= m:
                e = x - 1
            else:
                s = x + 1

        return s

        
```

---
*Generated automatically by LeetFeedback Extension*
