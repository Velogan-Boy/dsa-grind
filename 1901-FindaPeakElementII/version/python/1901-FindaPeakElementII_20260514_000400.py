# Last updated: 5/14/2026, 12:04:00 AM
1class Solution:
2    def findPeakGrid(self, mat):
3        m, n = len(mat), len(mat[0])
4
5        for i in range(m):
6            for j in range(n):
7                curr = mat[i][j]
8
9                up = mat[i - 1][j] if i > 0 else -1
10                down = mat[i + 1][j] if i < m - 1 else -1
11                left = mat[i][j - 1] if j > 0 else -1
12                right = mat[i][j + 1] if j < n - 1 else -1
13
14                if curr > up and curr > down and curr > left and curr > right:
15                    return [i, j]