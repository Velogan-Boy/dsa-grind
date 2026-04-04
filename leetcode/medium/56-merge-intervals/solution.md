# Merge Intervals

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/merge-intervals/submissions/1968833928/
- **Date:** 2026-04-04

## Solution

```python
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals: return []

        intervals.sort(key = lambda x : x[0])

        merged = intervals[0:1]

        for i in range(1, len(intervals)):
            if merged[-1][1] >= intervals[i][0]:
                merged[-1][0] = min(merged[-1][0], intervals[i][0])
                merged[-1][1] = max(merged[-1][1], intervals[i][1])
            else:
                merged.append(intervals[i])

        return merged




        
```

---
*Generated automatically by LeetFeedback Extension*
