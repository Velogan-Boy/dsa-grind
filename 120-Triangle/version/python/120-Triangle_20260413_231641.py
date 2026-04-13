# Last updated: 4/13/2026, 11:16:41 PM
1class Solution:
2    def minimumTotal(self, triangle: List[List[int]]) -> int:
3        n = len(triangle)
4
5        dp = triangle[-1][:]   # copy last row
6
7        for i in range(n - 2, -1, -1):
8            for j in range(len(triangle[i])):
9                dp[j] = triangle[i][j] + min(dp[j], dp[j + 1])
10
11        return dp[0]