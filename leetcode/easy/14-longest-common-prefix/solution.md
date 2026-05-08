# Longest Common Prefix

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Easy
- **URL:** https://leetcode.com/problems/longest-common-prefix/submissions/1998314773/
- **Date:** 2026-05-08

## Solution

```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pref = strs[0]
        res = ""

        for i in range(len(pref)):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res
                
            res += s[i]

        return res
        

```

---
*Generated automatically by LeetFeedback Extension*
