# Single Number II

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/single-number-ii/submissions/1955664203/
- **Date:** 2026-03-22

## Solution

```python
class Solution:
  def singleNumber(self, nums: List[int]) -> int:
    ones = 0
    twos = 0

    for num in nums:
      ones ^= (num & ~twos)
      twos ^= (num & ~ones)

    return ones
```

---
*Generated automatically by LeetFeedback Extension*
