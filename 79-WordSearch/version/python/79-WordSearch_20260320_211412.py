# Last updated: 3/20/2026, 9:14:12 PM
1class Solution:
2    def func(self, board, i, j, word, k):
3        if k == len(word):
4            return True
5
6        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or word[k] != board[i][j]:
7            return False
8
9        temp = board[i][j]
10        board[i][j] = ' '
11
12        ans = (self.func(board, i + 1, j, word, k + 1) or
13               self.func(board, i - 1, j, word, k + 1) or
14               self.func(board, i, j + 1, word, k + 1) or
15               self.func(board, i, j - 1, word, k + 1))
16
17        board[i][j] = temp
18        
19        return ans
20
21    def exist(self, board, word):
22        for i in range(len(board)):
23            for j in range(len(board[0])):
24                if board[i][j] == word[0]:
25                    if self.func(board, i, j, word, 0):
26                        return True
27        return False
28