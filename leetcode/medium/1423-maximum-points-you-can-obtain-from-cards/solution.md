# Maximum Points You Can Obtain from Cards

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/submissions/1961913165/
- **Date:** 2026-03-28

## Solution

```python
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        lsum, rsum = 0,0
        
        for i in range(k): lsum += cardPoints[i]

        maxSum = lsum

        rIndex = len(cardPoints) - 1
        for i in range(k - 1, -1, -1):
            lsum -= cardPoints[i]
            rsum += cardPoints[rIndex]
            rIndex -= 1

            maxSum = max(maxSum, lsum + rsum)


        return maxSum

        
```

---
*Generated automatically by LeetFeedback Extension*
