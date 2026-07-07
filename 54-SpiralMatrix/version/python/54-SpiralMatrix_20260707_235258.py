# Last updated: 7/7/2026, 11:52:58 PM
1class Solution:
2    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
3
4        ans = []
5        m,n = len(matrix), len(matrix[0])
6        up, down, left, right = 0, m - 1, 0, n - 1
7
8        while up <= down and left <= right:
9            # left -> right
10            for i in range(left, right + 1):
11                ans.append(matrix[up][i])
12            up+=1
13
14            # up -> down
15            for i in range(up, down + 1):
16                ans.append(matrix[i][right])
17            right-=1
18
19
20            if up <= down:
21            # right -> left
22                for i in range(right, left - 1, -1):
23                    ans.append(matrix[down][i])
24                down-=1
25
26            if left <= right:
27            # down -> up
28                for i in range(down, up - 1, -1):
29                    ans.append(matrix[i][left])
30                left+=1
31
32        return ans
33
34            
35
36
37
38
39        