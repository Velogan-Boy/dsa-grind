# Count Number of Nice Subarrays

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/count-number-of-nice-subarrays/submissions/1961789927/
- **Date:** 2026-03-28

## Solution

```python
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        def countSubarrys(k):
            if k < 0: return 0

            n = len(nums)
            l, r = 0, 0
            countOdd = 0
            count = 0

            while r < n:
                if nums[r] % 2 == 1: 
                    countOdd += 1
                
                while countOdd > k:
                    if nums[l] % 2 == 1: countOdd -= 1
                    l+=1

                count += (r - l + 1)
                r+=1
            
            return count

        return countSubarrys(k) - countSubarrys(k - 1)










        
```

---
*Generated automatically by LeetFeedback Extension*
