# Maximum Length of Repeated Subarray

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/maximum-length-of-repeated-subarray/submissions/1979236652/
- **Date:** 2026-04-15

## Solution

```python
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        m = len(nums2)
        
        prev = [0] * (m + 1)

        ans = 0
        for i in range(1, n + 1):
            curr = [0] * (n + 1)
            for j in range(1, m + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    curr[j] = 1 + prev[j - 1]
                    ans = max(ans, curr[j])
                else:
                    curr[j] = 0

            prev = curr
        
        return ans
        
```

---
*Generated automatically by LeetFeedback Extension*
