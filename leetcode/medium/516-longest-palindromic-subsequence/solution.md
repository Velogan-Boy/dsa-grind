# Longest Palindromic Subsequence

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/longest-palindromic-subsequence/submissions/1979239549/
- **Date:** 2026-04-15

## Solution

```python
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        return self.lcs(s, s[::-1])


    def lcs(self, str1, str2):
        m,n = len(str1), len(str2)

        memo = [[-1] * n for _ in range(m)]

        def dfs(i, j):
            if i < 0 or j < 0: return 0

            if memo[i][j] != -1: return memo[i][j]

            if str1[i] == str2[j]:
                memo[i][j] =  1 + dfs(i - 1, j - 1)
            else:
                memo[i][j] = max(dfs(i - 1, j), dfs(i, j - 1))
            
            return memo[i][j]
        
        return dfs(m - 1, n - 1)

```

---
*Generated automatically by LeetFeedback Extension*
