# Counting Bits

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Easy
- **URL:** https://leetcode.com/problems/counting-bits/submissions/2009267839/
- **Date:** 2026-05-21

## Solution

```python
class Solution:
    def countBits(self, n: int) -> List[int]:

        arr = [0] * (n + 1)

        for i in range(n + 1):
            num = i

            # find number of set bits
            count = 0

            while num:
                num = num & (num - 1)
                count += 1
            
            arr[i] = count
        
        return arr

        

        
```

---
*Generated automatically by LeetFeedback Extension*
