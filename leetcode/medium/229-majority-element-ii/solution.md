# Majority Element II

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/majority-element-ii/submissions/2000316932/
- **Date:** 2026-05-11

## Solution

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        count = defaultdict(int)
        n = len(nums)
        ans = set()

        for num in nums:
            count[num] += 1

            if count[num] > n // 3:
                ans.add(num)
            
        return list(ans)




        
```

---
*Generated automatically by LeetFeedback Extension*
