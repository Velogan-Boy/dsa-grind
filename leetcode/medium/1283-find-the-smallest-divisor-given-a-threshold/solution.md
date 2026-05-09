# Find the Smallest Divisor Given a Threshold

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/submissions/1998759313/
- **Date:** 2026-05-09

## Solution

```python
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        if threshold == 0:
            return 1

        s = 1
        e = max(nums)

        while s <= e:
            x = (s + e) // 2

            sumOfResult = 0
            for num in nums:
                sumOfResult += math.ceil(num / x)

            if sumOfResult <= threshold:
                e = x - 1
            else:
                s = x + 1

        return s
```

---
*Generated automatically by LeetFeedback Extension*
