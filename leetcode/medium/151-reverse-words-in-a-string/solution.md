# Reverse Words in a String

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/reverse-words-in-a-string/
- **Date:** 2026-04-28

## Solution

```python
class Solution:
    def reverseWords(self, s: str) -> str:  
        i,j, ans, n = 0, 0, '', len(s)

        while i < n:
            while i < n and s[i] == ' ': i+=1
            if i >= n: break

            j = i + 1
            while j < n and s[j] != ' ': j+=1

            if ans:
                ans = s[i:j] + ' ' + ans
            else:
                ans = s[i:j]

            i = j + 1

        return ans



        
```

---
*Generated automatically by LeetFeedback Extension*
