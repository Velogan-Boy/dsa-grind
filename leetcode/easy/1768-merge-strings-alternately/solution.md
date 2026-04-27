# Merge Strings Alternately

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Easy
- **URL:** https://leetcode.com/problems/merge-strings-alternately/submissions/1989527654/
- **Date:** 2026-04-27

## Solution

```python
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        m, n = len(word1), len(word2)
        res = []

        while i < m and j < n:
            res.append(word1[i])
            res.append(word2[j])
            i += 1
            j += 1

        if i < m:
            res.append(word1[i:])
        if j < n:
            res.append(word2[j:])

        return "".join(res)
```

---
*Generated automatically by LeetFeedback Extension*
