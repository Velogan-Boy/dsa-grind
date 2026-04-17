# Distinct Subsequences

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Hard
- **URL:** https://leetcode.com/problems/distinct-subsequences/submissions/1980758997/
- **Date:** 2026-04-17

## Solution

```python
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m,n = len(s), len(t)

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            dp[i][n] = 1

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if s[i] == t[j]:
                    dp[i][j] = dp[i + 1][j + 1] + dp[i + 1][j]
                else:
                    dp[i][j] = dp[i+1][j]

        
        return dp[0][0]
```

---
*Generated automatically by LeetFeedback Extension*
