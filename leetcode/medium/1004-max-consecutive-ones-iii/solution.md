# Max Consecutive Ones III

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/max-consecutive-ones-iii/
- **Date:** 2026-03-28

## Solution

```python
class Solution:
    def longestOnes(self, nums, k):
        l, r = 0, 0
        n = len(nums)
        ans = 0
        zeroes = 0

        while r < n:
            if nums[r] == 0: zeroes+=1

            if zeroes > k:
                if nums[l] == 0: zeroes-=1

            ans = max(ans, r - l + 1)
            r+=1

        return ans



            
            

                
```

---
*Generated automatically by LeetFeedback Extension*
