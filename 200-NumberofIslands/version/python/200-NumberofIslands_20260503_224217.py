# Last updated: 5/3/2026, 10:42:17 PM
1class Solution:
2    def numIslands(self, grid: List[List[str]]) -> int:
3        m,n = len(grid), len(grid[0])
4        visited = [[0] * n for _ in range(m)]
5
6        def dfs(x,y):
7            if visited[x][y]: return
8            visited[x][y] = 1
9
10            for dx, dy in [(-1,0),(0,-1),(0,1),(1,0)]:
11                xx, yy = x + dx, y + dy
12
13                if 0 <= xx < m and 0 <= yy < n and grid[xx][yy] == '1':
14                    dfs(xx,yy)
15
16        cnt = 0
17        for i in range(m):
18            for j in range(n):
19                if visited[i][j] != 1 and grid[i][j] == '1':
20                    dfs(i,j)
21                    cnt+=1
22
23        return cnt
24                
25
26
27
28
29
30
31
32        