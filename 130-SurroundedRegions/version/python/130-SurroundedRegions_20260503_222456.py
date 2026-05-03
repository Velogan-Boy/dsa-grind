# Last updated: 5/3/2026, 10:24:56 PM
1class Solution:
2    def solve(self, board: List[List[str]]) -> None:
3        m, n = len(board), len(board[0])
4        visited = [[0] * n for _ in range(m)]
5
6        def dfs(x, y):
7            if visited[x][y]: return
8            visited[x][y] = 1
9
10            for dx, dy in [(0,-1), (-1,0), (0,1),(1,0)]:
11                xx, yy = x + dx, y + dy
12
13                if 0 <= xx < m and 0 <= yy < n and board[xx][yy] == 'O':
14                    dfs(xx,yy)
15        
16
17        for j in range(n):
18            if board[0][j] == 'O':
19                dfs(0, j)
20            
21            if board[m - 1][j] == 'O':
22                dfs(m - 1,j)
23        
24        for i in range(m):
25            if board[i][0] == 'O':
26                dfs(i, 0)
27
28            if board[i][n - 1] == 'O':
29                dfs(i, n -1)
30        
31        for i in range(m):
32            for j in range(n):
33                if board[i][j] == 'O' and visited[i][j] == 0:
34                    board[i][j] = 'X'
35
36        return board
37        