# Boats to Save People

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/boats-to-save-people/submissions/2085092144/
- **Date:** 2026-07-28

## Solution

```python
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        i, j = 0, len(people) - 1
        boats = 0

        while i <= j:
            if people[i] + people[j] <= limit:
                i += 1
            j -= 1
            boats += 1

        return boats
```

---
*Generated automatically by LeetFeedback Extension*
