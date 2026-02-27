# Last updated: 2/27/2026, 10:35:49 PM
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])

        prev = [0] * n

        for i in range(m):
            curr = [0] * n

            for j in range(n):

                if i == 0 and j == 0: curr[j] = grid[i][j]
                else:
                    left = grid[i][j] + (curr[j - 1] if j > 0 else inf)
                    top = grid[i][j] + (prev[j] if i > 0 else inf)

                    curr[j] = min(left, top)


            prev = curr

        return prev[n - 1]
                

                


        