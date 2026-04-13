# Unique Paths II

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/unique-paths-ii/submissions/1977554770/
- **Date:** 2026-04-13

## Solution

```python
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m,n = len(obstacleGrid), len(obstacleGrid[0])

        memo = [[-1] * n for i in range(m)]

        def dfs(i,j):
            if i < 0 or j < 0: return 0
            if obstacleGrid[i][j]: return 0
            if i == 0 and j == 0: return 1 

            if memo[i][j] != -1: return memo[i][j]

            memo[i][j] = dfs(i - 1, j) + dfs(i, j - 1)

            return memo[i][j]

        return dfs(m - 1, n - 1)
        
```

---
*Generated automatically by LeetFeedback Extension*
