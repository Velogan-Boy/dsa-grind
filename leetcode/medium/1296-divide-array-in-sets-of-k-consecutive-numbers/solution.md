# Divide Array in Sets of K Consecutive Numbers

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/submissions/1976407651/
- **Date:** 2026-04-12

## Solution

```python
class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k != 0:
            return False

        count = Counter(nums)
        nums.sort()

        for card in nums:
            if count[card] == 0:
                continue

            for i in range(k):
                if count[card + i] == 0:
                    return False
                count[card + i] -= 1

        return True
        
```

---
*Generated automatically by LeetFeedback Extension*
