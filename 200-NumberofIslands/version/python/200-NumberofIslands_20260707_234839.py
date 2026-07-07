# Last updated: 7/7/2026, 11:48:39 PM
1class Solution:
2    def numIslands(self, grid: List[List[str]]) -> int:
3        m, n = len(grid), len(grid[0])
4
5        visited = [[0] * n for _ in range(m)]
6
7        def dfs(x, y):
8            if visited[x][y]: return
9            visited[x][y] = 1
10
11            for dx, dy in [(-1,0), (0, -1), (0, 1), (1, 0)]:
12                xx, yy = x + dx, y + dy
13
14                if xx >= 0 and xx < m and yy >= 0 and yy < n and grid[xx][yy] == '1':
15                    dfs(xx, yy)
16        
17        islands = 0
18        for i in range(m):
19            for j in range(n):
20                if grid[i][j] == '1' and visited[i][j] != 1:
21                    dfs(i, j)
22                    islands += 1
23
24        return islands
25
26                
27
28
29        