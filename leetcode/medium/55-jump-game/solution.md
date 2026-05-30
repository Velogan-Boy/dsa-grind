# Jump Game

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/jump-game/submissions/2017497226/
- **Date:** 2026-05-30

## Solution

```python
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxIndex = 0

        for i in range(len(nums)):
            if i > maxIndex: return False
            maxIndex = max(i + nums[i], maxIndex)


        return True

        
```

---
*Generated automatically by LeetFeedback Extension*
