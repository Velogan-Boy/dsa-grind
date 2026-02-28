# Last updated: 2/28/2026, 4:26:24 PM
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:

        dp = matrix[-1][:]

        for i in range(len(matrix)-2, -1, -1):
            new = [0]*len(dp)
            
            for j in range(len(dp)):
                new[j] = matrix[i][j] + min(
                    dp[j],
                    dp[j-1] if j > 0 else float('inf'),
                    dp[j+1] if j < len(dp)-1 else float('inf')
                )
            dp = new

        
        return min(dp)
        