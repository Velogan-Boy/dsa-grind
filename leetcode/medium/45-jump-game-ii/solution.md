# Jump Game II

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/jump-game-ii/submissions/1966122967/
- **Date:** 2026-04-01

## Solution

```python
class Solution:
    def jump(self, nums: List[int]) -> int:

        jumps = 0
        l, r = 0, 0
        n = len(nums)

        while r < n - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            
            l = r + 1
            r = farthest
            jumps+=1
        
        return jumps

        
```

---
*Generated automatically by LeetFeedback Extension*
