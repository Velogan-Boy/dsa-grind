# Gas Station

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/gas-station/submissions/2007293669/
- **Date:** 2026-05-19

## Solution

```python
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        start = 0
        tank = 0
        for i in range(len(gas)):
            tank += gas[i] - cost[i]

            if tank < 0:
                tank = 0
                start = i + 1
            
        return start



```

---
*Generated automatically by LeetFeedback Extension*
