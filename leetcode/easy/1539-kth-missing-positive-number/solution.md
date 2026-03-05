# Kth Missing Positive Number

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Easy
- **URL:** https://leetcode.com/problems/kth-missing-positive-number/submissions/1939009595/
- **Date:** 2026-03-05

## Solution

```python
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:

        hashSet = set(arr)

        curr = 0
        for x in range(1, max(arr) + k + 1):
            if x not in hashSet:
                curr+=1
            
            if curr == k: return x
                
        return max(arr) + k + 1
        
```

---
*Generated automatically by LeetFeedback Extension*
