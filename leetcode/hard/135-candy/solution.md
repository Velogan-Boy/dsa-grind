# Candy

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Hard
- **URL:** https://leetcode.com/problems/candy/submissions/1967749077/
- **Date:** 2026-04-03

## Solution

```python
class Solution:
    def candy(self, ratings: List[int]) -> int:

        n = len(ratings)

        left = [1] * n

        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                left[i] = left[i - 1] + 1
        
        right = 1
        ans = max(1, left[n-1])
        
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                curr = right + 1
            else:
                curr = 1
            
            right = curr
            
            ans += max(curr, left[i])

        return ans




        
```

---
*Generated automatically by LeetFeedback Extension*
