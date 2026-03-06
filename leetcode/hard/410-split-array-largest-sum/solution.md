# Split Array Largest Sum

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Hard
- **URL:** https://leetcode.com/problems/split-array-largest-sum/submissions/1939593518/
- **Date:** 2026-03-06

## Solution

```python
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        lowLimit = max(nums)
        upperLimit = sum(nums)

        while lowLimit <= upperLimit:
            maxSum = (lowLimit + upperLimit) // 2
            noOfSubarray = 1
            runningSum = 0

            for num in nums:
                if num + runningSum > maxSum:
                    noOfSubarray+=1
                    runningSum = num
                else:
                    runningSum += num

            if noOfSubarray <= k:
                upperLimit = maxSum - 1
            else:
                lowLimit = maxSum + 1

        return lowLimit

            



        
```

---
*Generated automatically by LeetFeedback Extension*
