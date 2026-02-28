# Last updated: 2/28/2026, 10:14:09 PM
1class Solution(object):
2    def findRotation(self, mat, target):
3        m = len(mat)
4        n = len(mat[0])
5
6        for _ in range(4):
7            for i in range(m):
8                for j in range(i, n):
9                    mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
10
11            for row in mat:
12                row.reverse()
13
14            if mat == target:
15                return True
16
17        return False