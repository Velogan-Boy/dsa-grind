# Distinct Subsequences

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Hard
- **URL:** https://leetcode.com/problems/distinct-subsequences/submissions/1980760741/
- **Date:** 2026-04-17

## Solution

```python
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m,n = len(s), len(t)

        prev = [0] * (n + 1)

        prev[n] = 1

        for i in range(m - 1, -1, -1):
            curr = [0] * (n + 1)
            curr[n] = 1

            for j in range(n - 1, -1, -1):
                if s[i] == t[j]:
                   curr[j] = prev[j + 1] + prev[j]
                else:
                   curr[j] = prev[j]

            prev = curr

        
        return prev[0]
```

---
*Generated automatically by LeetFeedback Extension*
