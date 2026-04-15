# Delete Operation for Two Strings

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/delete-operation-for-two-strings/submissions/1979265905/
- **Date:** 2026-04-15

## Solution

```python
class Solution:
    def minDistance(self, A: str, B: str) -> int:
        m, n = len(A), len(B)

        prev = [0] * (n + 1)

        for i in range(1, m + 1):
            curr = [0] * (n + 1)
            for j in range(1, n + 1):
                if A[i - 1] == B[j - 1]:
                    curr[j] = 1 + prev[j - 1]
                else:
                    curr[j] = max(prev[j], curr[j - 1])
            prev = curr

        lcs = prev[n]
        return (m - lcs) + (n - lcs)
```

---
*Generated automatically by LeetFeedback Extension*
