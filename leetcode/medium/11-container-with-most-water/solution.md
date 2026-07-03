# Container With Most Water

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/container-with-most-water/submissions/2054989818/
- **Date:** 2026-07-03

## Solution

```python
class Solution:
    def maxArea(self, height: List[int]) -> int:

        maxArea = 0

        l,r = 0, len(height) - 1

        while l < r:
            maxArea = max(maxArea, (r - l) * min(height[l], height[r]))

            if height[l] > height[r]: r-=1
            else: l +=1

        return maxArea

        
```

---
*Generated automatically by LeetFeedback Extension*
