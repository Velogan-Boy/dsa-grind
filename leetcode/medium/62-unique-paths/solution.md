# Unique Paths

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/unique-paths/submissions/2045541030/
- **Date:** 2026-06-25

## Solution

```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        @cache
        def dfs(i, j):
            if i == m - 1 and j == n - 1: return 1

            if i > m - 1 or j > n - 1: return 0

            return dfs(i + 1, j) + dfs(i, j + 1)

        return dfs(0,0)




        
```

---
*Generated automatically by LeetFeedback Extension*
