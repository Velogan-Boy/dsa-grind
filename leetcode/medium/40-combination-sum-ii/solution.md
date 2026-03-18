# Combination Sum II

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/combination-sum-ii/submissions/1951967127/
- **Date:** 2026-03-18

## Solution

```python
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def helper(i, currSum, curr):
            if currSum == 0:
                ans.append(curr[:])
                return

            if currSum < 0 or i == len(candidates):
                return
            
            curr.append(candidates[i])
            helper(i + 1, currSum - candidates[i], curr)

            curr.pop()
            for ind in range(i + 1, len(candidates)):
                if candidates[ind] != candidates[i]:
                    helper(ind, currSum, curr)
                    break


        candidates.sort()
        helper(0, target, [])

        return ans
```

---
*Generated automatically by LeetFeedback Extension*
