# Find the XOR of Numbers Which Appear Twice

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Easy
- **URL:** https://leetcode.com/problems/find-the-xor-of-numbers-which-appear-twice/submissions/1955570494/
- **Date:** 2026-03-22

## Solution

```python
from collections import defaultdict

class Solution:
    def duplicateNumbersXOR(self, nums):
        freq = defaultdict(int)
        xor = 0
        for num in nums:
            freq[num] += 1
            if freq[num] == 2:
                xor ^= num
        return xor
```

---
*Generated automatically by LeetFeedback Extension*
