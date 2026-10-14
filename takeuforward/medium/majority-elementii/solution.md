# Majority Element-II

## Problem Information
- **Platform:** Takeuforward
- **Difficulty:** Medium
- **URL:** https://takeuforward.org/practice/dsa/majority-element-ii
- **Date:** 2026-10-14

## Solution

```python
class Solution:
    def majorityElementTwo(self, nums):
        hm = {}

        for num in nums:
            hm[num] = hm.get(num, 0) + 1
        
        n = len(nums)   

        ans = []
        for key, value in hm.items():
            if value > n // 3:
                ans.append(key)

        return ans


        


        
```

---
*Generated automatically by LeetFeedback Extension*
