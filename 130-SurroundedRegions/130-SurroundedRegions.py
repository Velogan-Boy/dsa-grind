# Last updated: 2/28/2026, 4:28:28 PM
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])

        visited = [[0] * n for _ in range(m)]

        for j in range(n):
            if board[0][j] == 'O':
                self.dfs(board, 0, j, visited, m, n)
            
            if board[-1][j] == 'O':
                self.dfs(board, m - 1, j, visited, m, n)

        for i in range(m):
            if board[i][0] == 'O':
                self.dfs(board, i, 0, visited, m, n )

            if board[i][-1] == 'O':
                self.dfs(board, i, n - 1,visited, m, n)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and visited[i][j] != 1:
                    board[i][j] = 'X'

    

    def dfs(self, board, r, c, visited, m, n):

        if visited[r][c] == 1: return
        visited[r][c] = 1

        directions = [(-1,0), (0, -1), (0, 1), (1, 0)]

        for dr,dc in directions:
            nr, nc = r + dr, c + dc

            if 0 <= nr < m and 0 <= nc < n and visited[nr][nc] != 1 and board[nr][nc] == 'O' :
                self.dfs(board, nr, nc, visited,m,n)
