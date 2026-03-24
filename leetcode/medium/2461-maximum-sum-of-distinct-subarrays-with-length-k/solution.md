# Maximum Sum of Distinct Subarrays With Length K

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/submissions/1958036685/
- **Date:** 2026-03-24

## Solution

```python
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        currSum = 0
        l = 0
        r = 0
        hm = {}

        while r < len(nums):
            last_occurrence = hm.get(nums[r], -1)
            
            while l <= last_occurrence or r - l + 1 > k:
                currSum -= nums[l]
                l += 1
            hm[nums[r]] = r
            currSum += nums[r]
            if r - l + 1 == k:
                ans = max(ans, currSum)
            r += 1
        return ans
```

---
*Generated automatically by LeetFeedback Extension*
