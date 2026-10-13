# Kadane's Algorithm

## Problem Information
- **Platform:** Takeuforward
- **Difficulty:** Medium
- **URL:** https://takeuforward.org/practice/dsa/kadane's-algorithm
- **Date:** 2026-10-13

## Solution

```python
class Solution:
    def maxSubArray(self, nums):
        ans = float('-inf')
        currSum = 0

        for num in nums:
            if currSum < 0:
                currSum = num
            else:
                currSum += num

            ans = max(ans, currSum)

        return ans



            


```

---
*Generated automatically by LeetFeedback Extension*
