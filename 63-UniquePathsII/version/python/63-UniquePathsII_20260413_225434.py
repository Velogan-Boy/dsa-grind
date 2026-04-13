# Last updated: 4/13/2026, 10:54:34 PM
1class Solution:
2    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
3        m,n = len(obstacleGrid), len(obstacleGrid[0])
4
5        memo = [[-1] * n for i in range(m)]
6
7        def dfs(i,j):
8            if i < 0 or j < 0: return 0
9            if obstacleGrid[i][j]: return 0
10            if i == 0 and j == 0: return 1 
11
12            if memo[i][j] != -1: return memo[i][j]
13
14            memo[i][j] = dfs(i - 1, j) + dfs(i, j - 1)
15
16            return memo[i][j]
17
18        return dfs(m - 1, n - 1)
19        