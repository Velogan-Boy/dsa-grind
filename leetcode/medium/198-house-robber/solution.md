# House Robber

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/house-robber/
- **Date:** 2026-07-06

## Solution

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        @cache
        def dfs(i):

            if i >= n: return 0

            rob = dfs(i + 2) + nums[i]
            notRob = dfs(i + 1) + 0

            return max(rob, notRob) 

        return dfs(0)


        
```

---
*Generated automatically by LeetFeedback Extension*
