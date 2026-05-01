# Flood Fill

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Easy
- **URL:** https://leetcode.com/problems/flood-fill/submissions/
- **Date:** 2026-05-01

## Solution

```python
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m,n = len(image), len(image[0])

        if image[sr][sc] == color:
            return image

        srcColor = image[sr][sc]
        q = deque()
        q.append((sr,sc))
        visited = set((sr,sc))
        image[sr][sc] = color

        while q:
            x, y = q.popleft()

            for dx,dy in [(0,1), (1,0), (-1,0), (0,-1)]:
                xx, yy = x + dx, y + dy

                if xx < 0 or xx >= m or yy < 0 or yy >= n:
                    continue
                
                if (xx,yy) in visited: continue

                if image[xx][yy] == srcColor:
                    image[xx][yy] = color
                    visited.add((xx,yy))
                    q.append((xx,yy))

        return image








        
```

---
*Generated automatically by LeetFeedback Extension*
