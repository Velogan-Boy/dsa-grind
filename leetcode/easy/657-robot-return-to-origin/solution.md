# Robot Return to Origin

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Easy
- **URL:** https://leetcode.com/problems/robot-return-to-origin/submissions/1969545354/
- **Date:** 2026-04-05

## Solution

```python
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        
        dMap = { "U": [0,1], "R": [1,0], "D": [0, -1], "L": [-1, 0] }

        origin = [0,0]
        for d in moves:
            origin[0] += dMap[d][0]
            origin[1] += dMap[d][1]

        return origin == [0,0]


        
```

---
*Generated automatically by LeetFeedback Extension*
