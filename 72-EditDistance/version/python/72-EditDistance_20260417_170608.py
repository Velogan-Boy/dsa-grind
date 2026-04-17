# Last updated: 4/17/2026, 5:06:08 PM
1class Solution:
2    def minDistance(self, word1: str, word2: str) -> int:
3        dp = [[-1] * len(word2) for _ in range(len(word1))]
4        return self.solve(word1, word2, 0, 0, dp)
5
6    def solve(self, w1, w2, i, j, dp):
7        if i == len(w1):
8            return len(w2) - j
9        if j == len(w2):
10            return len(w1) - i
11
12        if dp[i][j] != -1:
13            return dp[i][j]
14
15        if w1[i] == w2[j]:
16            dp[i][j] = self.solve(w1, w2, i+1, j+1, dp)
17        else:
18            dp[i][j] = 1 + min(
19                self.solve(w1, w2, i, j+1, dp),
20                self.solve(w1, w2, i+1, j, dp),
21                self.solve(w1, w2, i+1, j+1, dp)
22            )
23        return dp[i][j]