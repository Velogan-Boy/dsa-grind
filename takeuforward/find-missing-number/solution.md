# Find missing number

## Problem Information
- **Platform:** Takeuforward
- **Difficulty:** Unknown
- **URL:** https://takeuforward.org/plus/dsa/problems/find-missing-number
- **Date:** 2026-05-11

## Solution

```python
class Solution:
    def missingNumber(self, nums):

        nums.sort()
        n = len(nums)

        for i in range(n):
            if i != nums[i]: return i

        return n
        
```

---
*Generated automatically by LeetFeedback Extension*
