# Last updated: 2/28/2026, 4:26:16 PM
class Solution:
    def shortestCommonSupersequence(self, s1: str, s2: str) -> str:
        m, n = len(s1), len(s2)
        dp = [[0]*(n+1) for _ in range(m+1)]

        # build LCS dp
        for i in range(1, m+1):
            for j in range(1, n+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        # backtrack to build SCS
        i, j = m, n
        res = []

        while i > 0 and j > 0:
            if s1[i-1] == s2[j-1]:
                res.append(s1[i-1])
                i -= 1
                j -= 1
            elif dp[i-1][j] > dp[i][j-1]:
                res.append(s1[i-1])
                i -= 1
            else:
                res.append(s2[j-1])
                j -= 1

        # append leftovers
        while i > 0:
            res.append(s1[i-1])
            i -= 1
        while j > 0:
            res.append(s2[j-1])
            j -= 1

        return "".join(reversed(res))
