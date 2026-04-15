# Maximum Length of Repeated Subarray

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/maximum-length-of-repeated-subarray/submissions/1979235279/
- **Date:** 2026-04-15

## Solution

```python
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        m = len(nums2)
        
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        ans = 0
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                    ans = max(ans, dp[i][j])
                else:
                    dp[i][j] = 0
        
        return ans
        
```

---
*Generated automatically by LeetFeedback Extension*
