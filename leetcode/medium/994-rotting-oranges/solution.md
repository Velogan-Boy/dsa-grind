# Rotting Oranges

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/rotting-oranges/submissions/2016683333/
- **Date:** 2026-05-29

## Solution

```python
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])
        q = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))
        

        ans = -1
        while q:
            size = len(q)
            ans += 1

            for _ in range(size):
                x, y = q.popleft()
                
                for dx, dy in [(-1,0), (0,-1), (1,0), (0,1)]:
                    xx, yy = x + dx, y + dy

                    if xx >= 0 and xx < m and yy >= 0 and yy < n and grid[xx][yy] == 1:
                        grid[xx][yy] = 2
                        q.append((xx, yy))

            
            
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1



        return max(ans, 0)



        
```

---
*Generated automatically by LeetFeedback Extension*
