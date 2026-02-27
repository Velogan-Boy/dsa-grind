# Last updated: 2/27/2026, 5:19:17 PM
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        return self.lcs(s, s[::-1])
        
    def lcs(self, text1: str, text2: str) -> int:

        dp = [[-1] * len(text2) for _ in range(len(text1))]

        return self.recRun(text1,text2, 0, 0,dp)

    def recRun(self, text1, text2, i , j, dp):

        if i >= len(text1) or j >= len(text2):
            return 0
        
        if dp[i][j] != -1:
            return dp[i][j]

        if text1[i] == text2[j]:
            dp[i][j] = 1 + self.recRun(text1, text2, i + 1, j + 1,dp)
        
        else:
            dp[i][j] = max(self.recRun(text1,text2, i + 1, j,dp), self.recRun(text1, text2, i, j+ 1,dp) )

        return dp[i][j]
        

        