# Kth Missing Positive Number

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Easy
- **URL:** https://leetcode.com/problems/kth-missing-positive-number/
- **Date:** 2026-03-05

## Solution

```python
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        s = 0
        e = len(arr) - 1

        while s <= e:
            mid = (s + e) // 2

            missing = arr[mid] - (mid + 1)

            if missing < k:
                s = mid + 1
            else:
                e = mid - 1

        return s + k



        
```

---
*Generated automatically by LeetFeedback Extension*
