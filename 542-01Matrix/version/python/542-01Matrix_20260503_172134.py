# Last updated: 5/3/2026, 5:21:34 PM
1from collections import deque
2
3class Solution:
4    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
5        m, n = len(mat), len(mat[0])
6
7        visited = [[0]*n for _ in range(m)]
8        ans = [[0]*n for _ in range(m)]
9
10        queue = deque()
11
12        for i in range(m):
13            for j in range(n):
14                if mat[i][j] == 0:
15                    queue.append((i, j, 0))
16                    visited[i][j] = 1
17        
18
19        while queue:
20            r,c,level = queue.popleft()
21            ans[r][c] = level
22
23            for dr, dc in [(-1,0), (0, -1), (1,0), (0,1)]:
24                nr,nc = r + dr, c + dc
25
26                if 0 <= nr < m and 0 <= nc < n and visited[nr][nc] == 0:
27                    queue.append((nr,nc, level + 1))
28                    visited[nr][nc] = 1
29            
30
31        return ans
32                
33
34
35
36
37
38
39        