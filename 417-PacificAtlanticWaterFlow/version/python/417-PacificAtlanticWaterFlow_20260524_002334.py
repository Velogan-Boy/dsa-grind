# Last updated: 5/24/2026, 12:23:34 AM
1class Solution:
2    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
3
4        m,n = len(heights), len(heights[0])
5
6        visited1 = [[0] * n for _ in range(m)]
7        visited2 = [[0] * n for _ in range(m)]
8
9        def dfs(x, y, visited):
10            if visited[x][y]: return 
11            visited[x][y] = 1
12
13            for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
14                xx, yy = x + dx, y + dy
15
16                if xx >= 0 and xx < m and yy >= 0 and yy < n and heights[xx][yy] >= heights[x][y]:
17                    dfs(xx,yy, visited)
18        
19       
20        for i in range(m):
21            if visited1[i][0] != 1:
22                dfs(i, 0, visited1)
23
24        for j in range(n):
25            if visited1[0][j] != 1:
26                dfs(0,j, visited1)
27
28        for i in range(m):
29            if visited2[i][n - 1] != 1:
30                dfs(i, n - 1, visited2)
31
32        for j in range(n):
33            if visited2[m - 1][j] != 1:
34                dfs(m - 1,j,  visited2)
35
36        ans = []
37        for i in range(m):
38            for j in range(n):
39                if visited1[i][j] and visited2[i][j]:
40                    ans.append([i,j])
41
42        return ans
43
44            
45        
46
47
48
49
50
51
52        