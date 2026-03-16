# Count all subsequences with sum K

## Problem Information
- **Platform:** Takeuforward
- **Difficulty:** Unknown
- **URL:** https://takeuforward.org/plus/dsa/problems/count-all-subsequences-with-sum-k
- **Date:** 2026-03-16

## Solution

```python
class Solution:
    def func(self, ind, sum, nums):
        if sum == 0:
            return 1
        if sum < 0 or ind == len(nums):
            return 0

        return self.func(ind + 1, sum - nums[ind], nums) + self.func(ind + 1, sum, nums)

    def countSubsequenceWithTargetSum(self, nums, target):
        return self.func(0, target, nums)

```

---
*Generated automatically by LeetFeedback Extension*
