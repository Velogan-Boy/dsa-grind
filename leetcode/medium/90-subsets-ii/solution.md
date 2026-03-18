# Subsets II

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/subsets-ii/submissions/1952038792/
- **Date:** 2026-03-18

## Solution

```python
class Solution:
    def func(self, ind, arr, nums, ans):
        if ind == len(nums):
            ans.append(arr.copy())
            return
        
        arr.append(nums[ind])
        self.func(ind + 1, arr, nums, ans)
        arr.pop()
        
        for j in range(ind + 1, len(nums)):
            if nums[j] != nums[ind]:
                self.func(j, arr, nums, ans)
                return
        
        ans.append(arr.copy())
    
    def subsetsWithDup(self, nums):
        ans = [] 
        arr = [] 
        nums.sort()  
        self.func(0, arr, nums, ans)  
        return ans

```

---
*Generated automatically by LeetFeedback Extension*
