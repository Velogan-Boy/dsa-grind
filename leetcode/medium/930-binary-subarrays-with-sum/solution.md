# Binary Subarrays With Sum

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/binary-subarrays-with-sum/submissions/1960050547/
- **Date:** 2026-03-26

## Solution

```python
class Solution:
    def numSubarraysWithSum(self, nums, goal):
        
        def func(myGoal):
            if myGoal < 0: return 0

            n = len(nums)
            l, r = 0, 0
            sum = 0
            count = 0

            while r < n:
                sum += nums[r]

                while sum > myGoal:
                    sum-= nums[l]
                    l+=1

                count+= (r - l + 1)
                r+=1


            return count

        return func(goal) - func(goal - 1)
```

---
*Generated automatically by LeetFeedback Extension*
