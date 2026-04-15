# Shortest Common Supersequence

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Hard
- **URL:** https://leetcode.com/problems/shortest-common-supersequence/submissions/1979271928/
- **Date:** 2026-04-15

## Solution

```python
class Solution:
    def lcs_dp(self, A, B):
        m, n = len(A), len(B)
        dp = [[0]*(n+1) for _ in range(m+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                if A[i-1] == B[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp
  
    def shortestCommonSupersequence(self, A: str, B: str) -> str:
        dp = self.lcs_dp(A, B)
        i, j = len(A), len(B)
        res = []

        while i > 0 and j > 0:
            if A[i-1] == B[j-1]:
                res.append(A[i-1])
                i -= 1
                j -= 1
            elif dp[i-1][j] > dp[i][j-1]:
                res.append(A[i-1])
                i -= 1
            else:
                res.append(B[j-1])
                j -= 1

        while i > 0:
            res.append(A[i-1])
            i -= 1
        while j > 0:
            res.append(B[j-1])
            j -= 1

        return "".join(reversed(res))
```

---
*Generated automatically by LeetFeedback Extension*
