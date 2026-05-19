# Valid Anagram

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Easy
- **URL:** https://leetcode.com/problems/valid-anagram/submissions/2007359460/
- **Date:** 2026-05-19

## Solution

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashMap = defaultdict(int)

        for ch in s:
            hashMap[ch]+=1
        
        for ch in t:
            hashMap[ch]-=1
        
        for k in hashMap.keys():
            if hashMap[k] != 0: return False
        
        return True
        
```

---
*Generated automatically by LeetFeedback Extension*
