# Last updated: 2/28/2026, 7:16:42 PM
1class Solution:
2    def setZeroes(self, matrix: List[List[int]]) -> None:
3        m,n = len(matrix), len(matrix[0])
4
5        col0 = 1
6        
7        for i in range(m):
8            for j in range(n):
9                if matrix[i][j] == 0:
10                    matrix[i][0] = 0
11
12                    if j != 0:
13                        matrix[0][j] = 0
14                    else: col0 = 0
15
16        
17        for i in range(1,m):
18            for j in range(1,n):
19                if matrix[i][0] == 0 or matrix[0][j] == 0:
20                    matrix[i][j] = 0
21
22        
23        if matrix[0][0] == 0:
24            for j in range(n):
25                matrix[0][j] = 0
26
27        if col0 == 0:
28            for i in range(m):
29                matrix[i][0] = 0
30
31        
32
33