# Jump Game

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/jump-game/submissions/1966106110/
- **Date:** 2026-04-01

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
