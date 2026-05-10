# Maximum Sum Circular Subarray

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/maximum-sum-circular-subarray/submissions/1999695127/
- **Date:** 2026-05-10

## Solution

```python
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        globMax, globMin = nums[0], nums[0]
        curMax, curMin = 0, 0
        total = 0
        
        for i, n in enumerate(nums):
            curMax = max(curMax + n, n)
            curMin = min(curMin + n, n)
            total += n
            globMax = max(curMax, globMax)
            globMin = min(curMin, globMin)

        return max(globMax, total - globMin) if globMax > 0 else globMax

```

---
*Generated automatically by LeetFeedback Extension*
