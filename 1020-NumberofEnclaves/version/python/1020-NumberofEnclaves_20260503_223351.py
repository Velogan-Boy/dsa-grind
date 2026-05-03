# Last updated: 5/3/2026, 10:33:51 PM
1class Solution:
2    def numEnclaves(self, grid: List[List[int]]) -> int:
3        m,n = len(grid), len(grid[0])
4        visited = [[0] * n for _ in range(m)]
5
6        def dfs(x, y):
7            if visited[x][y]: return 
8            visited[x][y] = 1
9
10            for dx, dy in [(-1,0), (0,-1),(1,0),(0,1)]:
11                xx, yy = x + dx, y + dy
12
13                if 0 <= xx < m and 0 <= yy < n and grid[xx][yy] == 1:
14                    dfs(xx,yy)
15
16        for i in range(m):
17            if grid[i][0] == 1:
18                dfs(i, 0)
19            
20            if grid[i][n - 1] == 1:
21                dfs(i, n - 1)
22
23        for j in range(n):
24            if grid[0][j] == 1:
25                dfs(0,j)
26            
27            if grid[m - 1][j] == 1:
28                dfs(m - 1, j)
29
30        cnt = 0
31        for i in range(m):
32            for j in range(n):
33                if grid[i][j] == 1 and visited[i][j] != 1:
34                    cnt += 1
35
36        return cnt
37
38
39
40        