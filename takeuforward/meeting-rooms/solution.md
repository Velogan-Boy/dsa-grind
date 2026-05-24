# Meeting Rooms

## Problem Information
- **Platform:** Takeuforward
- **Difficulty:** Unknown
- **URL:** https://takeuforward.org/plus/dsa/problems/meeting-rooms
- **Date:** 2026-05-24

## Solution

```python
class Solution:
    def canAttendMeetings(self, intervals):
        n = len(intervals)

        intervals.sort(key = lambda x: x[0])

        for i in range(1, n):
            if intervals[i - 1][1] > intervals[i][0]:
                return False

        return True
```

---
*Generated automatically by LeetFeedback Extension*
