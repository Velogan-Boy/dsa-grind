# Minimum Insertion Steps to Make a String Palindrome

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Hard
- **URL:** https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/submissions/1979270855/
- **Date:** 2026-04-15

## Solution

```python
class Solution:
    def lcs_dp(A, B):
        m, n = len(A), len(B)
        dp = [[0]*(n+1) for _ in range(m+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                if A[i-1] == B[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp
        
    def minInsertions(self, s: str) -> int:
        t = s[::-1]
        n = len(s)

        prev = [0] * (n + 1)

        for i in range(1, n + 1):
            curr = [0] * (n + 1)
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    curr[j] = 1 + prev[j - 1]
                else:
                    curr[j] = max(prev[j], curr[j - 1])
            prev = curr

        lps = prev[n]
        return n - lps
```

---
*Generated automatically by LeetFeedback Extension*
