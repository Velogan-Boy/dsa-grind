# Longest Increasing Subsequence

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/longest-increasing-subsequence/
- **Date:** 2026-04-19

## Solution

```python
class Solution:
    def lengthOfLIS(self, nums):
        n = len(nums)

        dp = [[0] * (n + 1) for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for prev_idx in range(i - 1, -2, -1):

                notPick = dp[i + 1][prev_idx + 1]

                pick = 0
                if prev_idx == -1 or nums[i] > nums[prev_idx]:
                    pick = 1 + dp[i + 1][i + 1]

                dp[i][prev_idx + 1] = max(pick, notPick)

        return dp[0][0]
```

---
*Generated automatically by LeetFeedback Extension*
