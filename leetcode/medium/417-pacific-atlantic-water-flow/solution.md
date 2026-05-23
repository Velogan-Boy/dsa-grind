# Pacific Atlantic Water Flow

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/pacific-atlantic-water-flow/submissions/2011096816/
- **Date:** 2026-05-23

## Solution

```python
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        m,n = len(heights), len(heights[0])

        visited1 = [[0] * n for _ in range(m)]
        visited2 = [[0] * n for _ in range(m)]

        def dfs(x, y, visited):
            if visited[x][y]: return 
            visited[x][y] = 1

            for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                xx, yy = x + dx, y + dy

                if xx >= 0 and xx < m and yy >= 0 and yy < n and heights[xx][yy] >= heights[x][y]:
                    dfs(xx,yy, visited)
        
       
        for i in range(m):
            if visited1[i][0] != 1:
                dfs(i, 0, visited1)

        for j in range(n):
            if visited1[0][j] != 1:
                dfs(0,j, visited1)

        for i in range(m):
            if visited2[i][n - 1] != 1:
                dfs(i, n - 1, visited2)

        for j in range(n):
            if visited2[m - 1][j] != 1:
                dfs(m - 1,j,  visited2)

        ans = []
        for i in range(m):
            for j in range(n):
                if visited1[i][j] and visited2[i][j]:
                    ans.append([i,j])

        return ans

            
        






        
```

---
*Generated automatically by LeetFeedback Extension*
