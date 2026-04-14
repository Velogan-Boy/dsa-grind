# Partition Equal Subset Sum

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/partition-equal-subset-sum/submissions/1978062182/
- **Date:** 2026-04-14

## Solution

```python
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)
        if totalSum % 2 != 0: return False
        n = len(nums)

        target = totalSum // 2

        dp = [[False] * (target + 1) for _ in range(n)]

        for i in range(n):
            dp[i][0] = True

        if nums[0] <= target:
            dp[0][nums[0]] = True
        
        for i in range(1, n):
            for j in range(1, target + 1):
                notPick = dp[i - 1][j]

                pick = False
                if nums[i] <= j:
                    pick = dp[i - 1][j - nums[i]]

                dp[i][j] = pick or notPick


        return dp[n - 1][target]

```

---
*Generated automatically by LeetFeedback Extension*
