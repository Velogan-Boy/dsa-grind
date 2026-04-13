# Unique Paths II

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/unique-paths-ii/submissions/1977561982/
- **Date:** 2026-04-13

## Solution

```python
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        dp = [[0] * n for _ in range(m)]

        for i in range(m):
            if obstacleGrid[i][0] == 1:
                break
            dp[i][0] = 1

        for j in range(n):
            if obstacleGrid[0][j] == 1:
                break
            dp[0][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m - 1][n - 1]
```

---
*Generated automatically by LeetFeedback Extension*
