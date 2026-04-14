# Partition Equal Subset Sum

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/partition-equal-subset-sum/submissions/1978063323/
- **Date:** 2026-04-14

## Solution

```python
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)
        if totalSum % 2 != 0: return False
        n = len(nums)

        target = totalSum // 2

        prev = [False] * (target + 1) 
        prev[0] = True

        if nums[0] <= target:
            prev[nums[0]] = True
        
        for i in range(1, n):
            curr = [False] * (target + 1)
            curr[0] = True

            for j in range(1, target + 1):
                notPick = prev[j]

                pick = False
                if nums[i] <= j:
                    pick = prev[j - nums[i]]

                curr[j] = pick or notPick
            
            prev = curr


        return prev[target]

```

---
*Generated automatically by LeetFeedback Extension*
