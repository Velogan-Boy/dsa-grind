# Last updated: 4/13/2026, 11:12:04 PM
1class Solution:
2    def minPathSum(self, grid: List[List[int]]) -> int:
3        m, n = len(grid), len(grid[0])
4
5        prev = [0] * n
6
7        for i in range(m):
8            curr = [0] * n
9            for j in range(n):
10                if i == 0 and j == 0:
11                    curr[j] = grid[i][j]
12                else:
13                    up = prev[j] if i > 0 else float('inf')
14                    left = curr[j - 1] if j > 0 else float('inf')
15
16                    curr[j] = grid[i][j] + min(up, left)
17            prev = curr
18
19        return prev[n - 1]