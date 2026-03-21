# Last updated: 3/21/2026, 11:04:15 PM
1class Solution:
2    def solveSudoku(self, board: list[list[str]]) -> None:
3        n, N = 3, 9
4        rows = [[0] * (N + 1) for _ in range(N)]
5        cols = [[0] * (N + 1) for _ in range(N)]
6        boxes = [[0] * (N + 1) for _ in range(N)]
7        sudokuSolved = False
8
9        def couldPlace(d, row, col):
10            idx = (row // n) * n + col // n
11            return rows[row][d] + cols[col][d] + boxes[idx][d] == 0
12
13        def placeNumber(d, row, col):
14            idx = (row // n) * n + col // n
15            rows[row][d] += 1
16            cols[col][d] += 1
17            boxes[idx][d] += 1
18            board[row][col] = str(d)
19
20        def removeNumber(d, row, col):
21            idx = (row // n) * n + col // n
22            rows[row][d] -= 1
23            cols[col][d] -= 1
24            boxes[idx][d] -= 1
25            board[row][col] = '.'
26
27        def placeNextNumbers(row, col):
28            nonlocal sudokuSolved
29            if row == N - 1 and col == N - 1:
30                sudokuSolved = True
31            elif col == N - 1:
32                backtrack(row + 1, 0)
33            else:
34                backtrack(row, col + 1)
35
36        def backtrack(row, col):
37            nonlocal sudokuSolved
38            if board[row][col] == '.':
39                for d in range(1, 10):
40                    if couldPlace(d, row, col):
41                        placeNumber(d, row, col)
42                        placeNextNumbers(row, col)
43                        if not sudokuSolved:
44                            removeNumber(d, row, col)
45            else:
46                placeNextNumbers(row, col)
47
48        for i in range(N):
49            for j in range(N):
50                if board[i][j] != '.':
51                    placeNumber(int(board[i][j]), i, j)
52        backtrack(0, 0)