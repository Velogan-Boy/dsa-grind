# Number of Zero-Filled Subarrays

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/number-of-zero-filled-subarrays/submissions/2009992516/
- **Date:** 2026-05-22

## Solution

```python
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        i , j = 0, 0
        count = 0
        n = len(nums)

        while i < n and j < n:
            while i < n and nums[i] != 0 and i < n: i += 1
            j = i + 1

            if i >= n: break

            while j < n and nums[j] == 0: j += 1

            l = j - i

            count += l * (l + 1) // 2

            i = j + 1

        return count








        
```

---
*Generated automatically by LeetFeedback Extension*
