# Smallest Index With Equal Value

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Easy
- **URL:** https://leetcode.com/problems/smallest-index-with-equal-value/submissions/1939652289/
- **Date:** 2026-03-06

## Solution

```python
class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if i % 10 == nums[i]:
                return i
        
        return -1
        
```

---
*Generated automatically by LeetFeedback Extension*
