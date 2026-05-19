# Contains Duplicate

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Easy
- **URL:** https://leetcode.com/problems/contains-duplicate/submissions/2007392794/
- **Date:** 2026-05-19

## Solution

```python
class Solution(object):
    def containsDuplicate(self, nums):
        
        numSet = set(nums)

        if len(numSet) != len(nums): return True
        else: return False
        
```

---
*Generated automatically by LeetFeedback Extension*
