# Left Rotate Array by One

## Problem Information
- **Platform:** Takeuforward
- **Difficulty:** Unknown
- **URL:** https://takeuforward.org/plus/dsa/problems/left-rotate-array-by-one
- **Date:** 2026-05-11

## Solution

```python
class Solution:
    def rotateArrayByOne(self, nums):

        for i in range(len(nums) - 1):
            nums[i], nums[i + 1] = nums[i + 1], nums[i]

```

---
*Generated automatically by LeetFeedback Extension*
