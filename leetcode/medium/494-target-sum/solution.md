# Target Sum

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/target-sum/submissions/2083597265/
- **Date:** 2026-07-27

## Solution

```python
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        @cache
        def dfs(i, currSum):
            if i == n: return 1 if currSum == target else 0

            return dfs(i + 1, currSum - nums[i]) + dfs(i + 1, currSum + nums[i])

        return dfs(0, 0)

        
```

---
*Generated automatically by LeetFeedback Extension*
