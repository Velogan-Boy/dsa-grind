# Last updated: 2/27/2026, 9:37:13 PM
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m = len(triangle)
        dp = [0] * len(triangle[-1])

        for j in range(len(triangle[-1])):
            dp[j] = triangle[m - 1][j]

        for i in range(m - 2, -1, -1):
            for j in range(len(triangle[i])):
                dp[j] = triangle[i][j] + min(
                    dp[j],
                    dp[j+1]
                )
                


        return dp[0]

        
        