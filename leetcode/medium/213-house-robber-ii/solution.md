# House Robber II

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/house-robber-ii/submissions/1977300748/
- **Date:** 2026-04-13

## Solution

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        
        return max( self.robRec(nums[:-1]) , self.robRec(nums[1:]) )


    def robRec(self,nums):
        prev2 = 0 
        prev1 = 0 

        for money in nums:
            curr = max(prev1, prev2 + money)
            prev2 = prev1
            prev1 = curr

        return prev1
        
        
```

---
*Generated automatically by LeetFeedback Extension*
