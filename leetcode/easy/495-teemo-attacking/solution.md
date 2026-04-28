# Teemo Attacking

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Easy
- **URL:** https://leetcode.com/problems/teemo-attacking/submissions/1990446037/
- **Date:** 2026-04-28

## Solution

```python
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if duration == 0: return 0

        res = 0
        for i in range(len(timeSeries)):
            if i != len(timeSeries) - 1:
                res += min(duration, timeSeries[i + 1] - timeSeries[i])
            else:
                res += duration

        return res
            

        
```

---
*Generated automatically by LeetFeedback Extension*
