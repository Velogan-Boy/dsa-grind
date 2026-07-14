# Maximum Difference Between Increasing Elements

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Easy
- **URL:** https://leetcode.com/problems/maximum-difference-between-increasing-elements/submissions/2067751055/
- **Date:** 2026-07-14

## Solution

```python
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        
        n = len(nums)

        prefMin = [float("inf")] * n
        ans = -1

        for i, num in enumerate(nums):
            if i == 0: continue
            prefMin[i] = min(prefMin[i - 1], nums[i - 1])

            if prefMin[i] < num:
                ans = max(ans, num - prefMin[i])

        return ans
        






        
```

---
*Generated automatically by LeetFeedback Extension*
