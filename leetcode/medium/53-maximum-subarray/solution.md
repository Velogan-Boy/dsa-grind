# Maximum Subarray

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/maximum-subarray/submissions/2005422444/
- **Date:** 2026-05-17

## Solution

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)

        currSum = 0
        maxSum = -inf
        for num in nums:
            currSum += num
            maxSum = max(maxSum, currSum)
            if currSum < 0: currSum = 0
        
        return maxSum

        
```

---
*Generated automatically by LeetFeedback Extension*
