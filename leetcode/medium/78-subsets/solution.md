# Subsets

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/subsets/submissions/1955581504/
- **Date:** 2026-03-22

## Solution

```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        subsets = 1 << n
        ans = []

        for i in range(subsets):
            list = []
            for j in range(n):
                if i & (1 << j):
                    list.append(nums[j])

            ans.append(list)

        return ans


            
        
```

---
*Generated automatically by LeetFeedback Extension*
