# Longest Common Subsequence

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/longest-common-subsequence/submissions/2011779026/
- **Date:** 2026-05-24

## Solution

```python
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)

        dp = [[-1] * n for _ in range(m)]

        def dfs(i, j):
            if i < 0 or j < 0: return 0
            if dp[i][j] != -1: return dp[i][j]

            if text1[i] == text2[j]:
                dp[i][j] =  1 + dfs(i - 1, j - 1)
            else:
                dp[i][j] = max(dfs(i - 1, j), dfs(i, j - 1))

            return dp[i][j]

        
        return dfs(m - 1, n - 1)
        

        
```

---
*Generated automatically by LeetFeedback Extension*
