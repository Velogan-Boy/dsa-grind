# Last updated: 2/27/2026, 5:11:16 PM
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return

        m, n = len(grid), len(grid[0])
        visited = [[0] * n for _ in range(m)]

        for j in range(n):
            if grid[0][j] == 1:
                self.dfs(grid, 0, j, visited, m, n)
            if grid[m - 1][j] == 1:
                self.dfs(grid, m - 1, j, visited, m, n)

        for i in range(m):
            if grid[i][0] == 1:
                self.dfs(grid, i, 0, visited, m, n)
            if grid[i][n - 1] == 1:
                self.dfs(grid, i, n - 1, visited, m, n)

        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and visited[i][j] == 0:
                    cnt += 1


        return cnt
                    

    def dfs(self, grid, r, c, visited, m, n):
        visited[r][c] = 1

        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if (
                0 <= nr < m and
                0 <= nc < n and
                grid[nr][nc] == 1 and
                visited[nr][nc] == 0
            ):
                self.dfs(grid, nr, nc, visited, m, n)
