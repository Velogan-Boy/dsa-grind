# Last updated: 5/29/2026, 11:48:05 PM
1class Solution:
2    def orangesRotting(self, grid: List[List[int]]) -> int:
3
4        m, n = len(grid), len(grid[0])
5        q = deque()
6
7        for i in range(m):
8            for j in range(n):
9                if grid[i][j] == 2:
10                    q.append((i, j))
11        
12
13        ans = -1
14        while q:
15            size = len(q)
16            ans += 1
17
18            for _ in range(size):
19                x, y = q.popleft()
20                
21                for dx, dy in [(-1,0), (0,-1), (1,0), (0,1)]:
22                    xx, yy = x + dx, y + dy
23
24                    if xx >= 0 and xx < m and yy >= 0 and yy < n and grid[xx][yy] == 1:
25                        grid[xx][yy] = 2
26                        q.append((xx, yy))
27
28            
29            
30        for i in range(m):
31            for j in range(n):
32                if grid[i][j] == 1:
33                    return -1
34
35
36
37        return max(ans, 0)
38
39
40
41        