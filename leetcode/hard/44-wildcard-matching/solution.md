# Wildcard Matching

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Hard
- **URL:** https://leetcode.com/problems/wildcard-matching/submissions/1980890059/
- **Date:** 2026-04-17

## Solution

```python
class Solution:
    def isAllStars(self, S1, i):
        for j in range(i + 1):
            if S1[j] != '*':
                return False
        return True

    @cache
    def wildcardMatchingUtil(self, S1, S2, i, j):
        if i < 0 and j < 0:
            return True
        if i < 0 and j >= 0:
            return False
        if j < 0 and i >= 0:
            return self.isAllStars(S1, i)

        if S1[i] == S2[j] or S1[i] == '?':
            return self.wildcardMatchingUtil(S1, S2, i - 1, j - 1)

        if S1[i] == '*':
            return (self.wildcardMatchingUtil(S1, S2, i - 1, j) or
                    self.wildcardMatchingUtil(S1, S2, i, j - 1))
                    
        return False

    def isMatch(self, str, pat):
        n = len(str)
        m = len(pat)
        return self.wildcardMatchingUtil(pat, str, m - 1, n - 1)

```

---
*Generated automatically by LeetFeedback Extension*
