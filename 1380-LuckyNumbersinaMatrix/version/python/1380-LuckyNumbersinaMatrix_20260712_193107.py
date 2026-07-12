# Last updated: 7/12/2026, 7:31:07 PM
1class Solution:
2    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
3        m,n = len(matrix), len(matrix[0])
4
5        min_row = set()
6        max_col = set()
7
8        for i in range(m):
9            mini = float('inf')
10
11            for j in range(n):
12                if mini > matrix[i][j]:
13                    mini = matrix[i][j]
14            
15            min_row.add(mini)
16        
17        for j in range(n):
18            maxi = float('-inf')
19
20            for i in range(m):
21                if maxi < matrix[i][j]:
22                    maxi = matrix[i][j]
23                
24            max_col.add(maxi)
25
26        return list(min_row & max_col)
27
28
29
30        