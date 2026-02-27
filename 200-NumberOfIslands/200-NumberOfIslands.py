# Last updated: 2/27/2026, 5:19:31 PM
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n = len(grid), len(grid[0])
        visited = [[0] * n for _ in range(m)]
        
        cnt = 0

        for i in range(m):
            for j in range(n):
                if visited[i][j] != 1 and grid[i][j] != '0':
                    cnt+=1
                    self.bfs(grid,i,j,visited)
        
        return cnt

    
    def bfs(self, grid, i, j, visited):
        m, n = len(grid), len(grid[0])
        queue = deque()
        
        queue.append((i, j))
        visited[i][j] = 1

        while queue:
            r, c = queue.popleft()

            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                nr, nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n:
                    if grid[nr][nc] == '1' and visited[nr][nc] == 0:
                        visited[nr][nc] = 1
                        queue.append((nr, nc))


        







        