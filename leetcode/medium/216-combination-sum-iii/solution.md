# Combination Sum III

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/combination-sum-iii/submissions/1953310344/
- **Date:** 2026-03-19

## Solution

```python
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        nums = []
        self.func(n, 1, nums, k, ans)
        return ans


    def func(self, sum, last, nums, k, ans):
        if sum == 0 and len(nums) == k:
            ans.append(list(nums))
            return

        if sum <= 0 or len(nums) > k:
            return

        for i in range(last, 10):
            if i <= sum:
                nums.append(i)
                self.func(sum - i, i + 1, nums, k, ans)
                nums.pop()
            else:
                break

  
```

---
*Generated automatically by LeetFeedback Extension*
