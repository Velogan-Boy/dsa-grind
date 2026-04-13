# Unique Paths

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/unique-paths/submissions/1977536223/
- **Date:** 2026-04-13

## Solution

```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        memo = [[-1] * n for _ in range(m)]

        def dfs(i, j):
            if i < 0 or j < 0:
                return 0

            if i == 0 and j == 0:
                return 1
            
            if memo[i][j] != -1: return memo[i][j]
            
            right = dfs(i, j - 1)
            down = dfs(i - 1, j)

            memo[i][j] = right + down
            return memo[i][j]

        return dfs(m - 1, n - 1) 
        
```

---
*Generated automatically by LeetFeedback Extension*
