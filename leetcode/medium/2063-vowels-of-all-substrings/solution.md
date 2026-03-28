# Vowels of All Substrings

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/vowels-of-all-substrings/submissions/1961884743/
- **Date:** 2026-03-28

## Solution

```python
class Solution:
    def countVowels(self, word: str) -> int:
        n = len(word)
        count = 0

        for i in range(n):
            if word[i] in 'aeiou':
                count += (n - i) * (i + 1)

        return count                
        
```

---
*Generated automatically by LeetFeedback Extension*
