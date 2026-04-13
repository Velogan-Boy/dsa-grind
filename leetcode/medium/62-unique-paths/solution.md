# Unique Paths

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/unique-paths/submissions/1977543664/
- **Date:** 2026-04-13

## Solution

```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        dp = [[-1] * n for _ in range(m)]

        dp[0][0] = 1

        for j in range(n):
            dp[0][j] = 1

        for i in range(m):
            dp[i][0] = 1

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i][j- 1] + dp[i - 1][j]


        return dp[m - 1][n - 1] 
        
```

---
*Generated automatically by LeetFeedback Extension*
