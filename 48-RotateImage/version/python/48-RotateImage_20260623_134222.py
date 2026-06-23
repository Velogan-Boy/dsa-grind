# Last updated: 6/23/2026, 1:42:22 PM
1class Solution:
2    def rotate(self, matrix: List[List[int]]) -> None:
3        
4        for i in range(len(matrix) - 1):
5            for j in range(i + 1, len(matrix)):
6                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
7
8
9        for i in range(len(matrix)):
10            matrix[i].reverse()
11
12         
13        