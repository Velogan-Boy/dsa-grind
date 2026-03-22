# Single Number

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Easy
- **URL:** https://leetcode.com/problems/single-number/submissions/1955567319/
- **Date:** 2026-03-22

## Solution

```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        ans = 0
        for num in nums:
            ans ^= num

        return ans

        
```

---
*Generated automatically by LeetFeedback Extension*
