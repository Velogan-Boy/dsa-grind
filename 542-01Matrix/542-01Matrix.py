# Last updated: 2/27/2026, 10:35:09 PM
from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])

        visited = [[0]*n for _ in range(m)]
        ans = [[0]*n for _ in range(m)]

        queue = deque()

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i, j, 0))
                    visited[i][j] = 1
        

        while queue:
            r,c,level = queue.popleft()
            ans[r][c] = level

            for dr, dc in [(-1,0), (0, -1), (1,0), (0,1)]:
                nr,nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n and visited[nr][nc] == 0:
                    queue.append((nr,nc, level + 1))
                    visited[nr][nc] = 1
            

        return ans
                






        