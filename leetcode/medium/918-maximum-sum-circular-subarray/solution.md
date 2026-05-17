# Maximum Sum Circular Subarray

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/maximum-sum-circular-subarray/submissions/2005434185/
- **Date:** 2026-05-17

## Solution

```python
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = sum(nums)

        currMax = globalMax = nums[0]
        currMin = globalMin = nums[0]

        for num in nums[1:]:
            currMax = max(num, currMax + num)
            globalMax = max(globalMax, currMax)

            currMin = min(num, currMin + num)
            globalMin = min(globalMin, currMin)

        if globalMax < 0:
            return globalMax

        return max(globalMax, total - globalMin)
```

---
*Generated automatically by LeetFeedback Extension*
