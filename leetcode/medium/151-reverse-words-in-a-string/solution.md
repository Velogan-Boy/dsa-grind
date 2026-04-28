# Reverse Words in a String

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/reverse-words-in-a-string/submissions/1990462307/
- **Date:** 2026-04-28

## Solution

```python
class Solution:
    def reverseWords(self, s: str) -> str:  
        i,j, ans, n = 0, 0, '', len(s)

        while i < n:
            while i < n and s[i] == ' ': i+=1
            j = i
            while j < n and s[j] != ' ': j+=1

            w = s[i:j]

            if w:
                ans = w + ' ' + ans
                
            i = j

        return ans.strip()



        
```

---
*Generated automatically by LeetFeedback Extension*
