# Longest Increasing Subsequence

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/longest-increasing-subsequence/submissions/2019422332/
- **Date:** 2026-06-01

## Solution

```python
class Solution:
    def lengthOfLIS(self, nums):
        n = len(nums)

        dp = [1] * n

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)
```

---
*Generated automatically by LeetFeedback Extension*
