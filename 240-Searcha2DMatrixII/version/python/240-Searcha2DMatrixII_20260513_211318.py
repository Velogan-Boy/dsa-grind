# Last updated: 5/13/2026, 9:13:18 PM
1class Solution:
2    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
3        m,n = len(matrix), len(matrix[0])
4        row, col = 0, n - 1
5
6        while row < m and col >= 0:
7            if matrix[row][col] == target:
8                return True
9            
10            if matrix[row][col] < target:
11                row+=1
12            else:
13                col-=1
14        
15        return False
16         