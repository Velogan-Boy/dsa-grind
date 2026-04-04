# Insert Interval

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/insert-interval/submissions/1968806310/
- **Date:** 2026-04-04

## Solution

```python
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        if not intervals: return [newInterval]

        merged = []

        inserted = 0
        for start,end  in intervals:
            if start > newInterval[0] and inserted == 0:
                merged.append(newInterval)
                inserted = 1
            
            merged.append([start,end])

        if inserted == 0: merged.append(newInterval)

        ans = merged[0:1]
        for i in range(1, len(merged)):
            if ans[-1][1] >= merged[i][0]:
                ans[-1][0] = min(ans[-1][0], merged[i][0]) 
                ans[-1][1] = max(ans[-1][1], merged[i][1])  
            else:
                ans.append(merged[i])


        return ans
            

        
```

---
*Generated automatically by LeetFeedback Extension*
