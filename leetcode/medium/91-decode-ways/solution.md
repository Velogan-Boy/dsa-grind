# Decode Ways

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/decode-ways/submissions/2019985166/
- **Date:** 2026-06-02

## Solution

```python
class Solution:
    def numDecodings(self, s: str) -> int:
        
        n = len(s)

        @cache
        def dfs(i):
            if i == n: return 1

            l,r = 0, 0
            if s[i] != '0':
                l = dfs(i + 1)
            
            if s[i] != '0' and i != n - 1 and int(s[i] + s[i + 1]) <= 26:
                r = dfs(i + 2)
            
            return l + r

        return dfs(0)



        
```

---
*Generated automatically by LeetFeedback Extension*
