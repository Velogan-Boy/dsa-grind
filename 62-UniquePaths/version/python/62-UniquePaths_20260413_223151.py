# Last updated: 4/13/2026, 10:31:51 PM
1class Solution:
2    def uniquePaths(self, m: int, n: int) -> int:
3
4        memo = [[-1] * n for _ in range(m)]
5
6        def dfs(i, j):
7            if i < 0 or j < 0:
8                return 0
9
10            if i == 0 and j == 0:
11                return 1
12            
13            if memo[i][j] != -1: return memo[i][j]
14            
15            right = dfs(i, j - 1)
16            down = dfs(i - 1, j)
17
18            memo[i][j] = right + down
19            return memo[i][j]
20
21        return dfs(m - 1, n - 1) 
22        