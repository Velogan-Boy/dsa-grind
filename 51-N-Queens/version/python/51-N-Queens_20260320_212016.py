# Last updated: 3/20/2026, 9:20:16 PM
1class Solution:
2    def isSafe(self, board, row, col):
3        r, c = row, col
4
5        while r >= 0 and c >= 0:
6            if board[r][c] == "Q":
7                return False
8            r -= 1
9            c -= 1
10
11        r, c = row, col
12
13        while r >= 0:
14            if board[r][c] == "Q":
15                return False
16            r -= 1
17
18        r, c = row, col
19
20        while r >= 0 and c < len(board[0]):
21            if board[r][c] == "Q":
22                return False
23            r -= 1
24            c += 1
25
26        return True
27
28    def func(self, row, ans, board):
29        if row == len(board):
30            ans.append(["".join(r) for r in board])
31            return
32
33        for col in range(len(board[0])):
34            if self.isSafe(board, row, col):
35                board[row][col] = "Q"
36
37                self.func(row + 1, ans, board)
38
39                board[row][col] = "."
40
41    def solveNQueens(self, n):
42        ans = []
43        board = [["." for _ in range(n)] for _ in range(n)]
44
45        self.func(0, ans, board)
46        return ans
47