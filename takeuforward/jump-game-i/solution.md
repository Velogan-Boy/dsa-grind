# Jump Game - I

## Problem Information
- **Platform:** Takeuforward
- **Difficulty:** Unknown
- **URL:** https://takeuforward.org/plus/dsa/problems/jump-game---i
- **Date:** 2026-05-17

## Solution

```python
class Solution:
    def canJump(self, nums):
        farthest = 0

        for i in range(len(nums)):
            if i > farthest:
                return False

            farthest = max(farthest, i + nums[i])

        return True
```

---
*Generated automatically by LeetFeedback Extension*
