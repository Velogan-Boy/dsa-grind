# Partition Equal Subset Sum

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/partition-equal-subset-sum/submissions/1978057009/
- **Date:** 2026-04-14

## Solution

```python
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)
        if totalSum % 2 != 0: return False
        n = len(nums)

        target = totalSum // 2

        memo = [[-1] * (target + 1) for _ in range(n)]

        def dfs(i, target):
            if memo[i][target] != -1: return memo[i][target]

            if target < 0: return False
            if target == 0: 
                memo[i][target] = True
                return memo[i][target]

            if i < 0: return False

            pick = dfs(i - 1, target - nums[i])
            notPick = dfs(i - 1, target)

            memo[i][target] =  pick or notPick

            return memo[i][target]

        return dfs(n - 1, target)

```

---
*Generated automatically by LeetFeedback Extension*
