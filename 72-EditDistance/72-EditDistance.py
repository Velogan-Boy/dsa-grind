# Last updated: 7/12/2026, 6:24:03 PM
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[-1] * len(word2) for _ in range(len(word1))]
        return self.solve(word1, word2, 0, 0, dp)

    def solve(self, w1, w2, i, j, dp):
        if i == len(w1):
            return len(w2) - j
        if j == len(w2):
            return len(w1) - i

        if dp[i][j] != -1:
            return dp[i][j]

        if w1[i] == w2[j]:
            dp[i][j] = self.solve(w1, w2, i+1, j+1, dp)
        else:
            dp[i][j] = 1 + min(
                self.solve(w1, w2, i, j+1, dp),
                self.solve(w1, w2, i+1, j, dp),
                self.solve(w1, w2, i+1, j+1, dp)
            )
        return dp[i][j]