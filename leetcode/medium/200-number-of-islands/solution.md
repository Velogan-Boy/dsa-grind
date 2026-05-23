# Number of Islands

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/number-of-islands/submissions/2011042096/
- **Date:** 2026-05-23

## Solution

```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        visited = [[0] * n for _ in range(m)]

        def dfs(x, y):
            if visited[x][y]: return
            visited[x][y] = 1

            for dx, dy in [(-1,0), (0, -1), (0, 1), (1, 0)]:
                xx, yy = x + dx, y + dy

                if xx >= 0 and xx < m and yy >= 0 and yy < n and grid[xx][yy] == '1':
                    dfs(xx, yy)
        
        islands = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and visited[i][j] != 1:
                    dfs(i, j)
                    islands += 1

        return islands

                


        
```

---
*Generated automatically by LeetFeedback Extension*
