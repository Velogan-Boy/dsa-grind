# Contains Duplicate II

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Easy
- **URL:** https://leetcode.com/problems/contains-duplicate-ii/submissions/2007398144/
- **Date:** 2026-05-19

## Solution

```python
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        last_seen = {}

        for i, num in enumerate(nums):
            if num in last_seen and i - last_seen[num] <= k:
                return True
            last_seen[num] = i

        return False
```

---
*Generated automatically by LeetFeedback Extension*
