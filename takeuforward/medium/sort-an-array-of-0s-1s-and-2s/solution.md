# Sort an array of 0's 1's and 2's

## Problem Information
- **Platform:** Takeuforward
- **Difficulty:** Medium
- **URL:** https://takeuforward.org/practice/dsa/sort-an-array-of-0's-1's-and-2's
- **Date:** 2026-10-15

## Solution

```python
class Solution:
    def sortZeroOneTwo(self, nums):
        freq = [0] * 3
        
        for num in nums:
            freq[num] += 1
        
        i = 0
        for num in range(3):
            count = freq[num]
            while count > 0:
                nums[i] = num
                i += 1
                count -= 1
```

---
*Generated automatically by LeetFeedback Extension*
