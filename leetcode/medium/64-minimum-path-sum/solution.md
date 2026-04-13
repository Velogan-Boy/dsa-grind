# Minimum Path Sum

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/minimum-path-sum/submissions/1977580183/
- **Date:** 2026-04-13

## Solution

```python
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        prev = [0] * n

        for i in range(m):
            curr = [0] * n
            for j in range(n):
                if i == 0 and j == 0:
                    curr[j] = grid[i][j]
                else:
                    up = prev[j] if i > 0 else float('inf')
                    left = curr[j - 1] if j > 0 else float('inf')

                    curr[j] = grid[i][j] + min(up, left)
            prev = curr

        return prev[n - 1]
```

---
*Generated automatically by LeetFeedback Extension*
