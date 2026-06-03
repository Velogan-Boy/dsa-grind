# Maximum Product Subarray

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/maximum-product-subarray/submissions/2021593118/
- **Date:** 2026-06-03

## Solution

```python
class Solution:
    def maxProduct(self, arr):
        n = len(arr)

        pre, suff = 1, 1

        ans = float('-inf')

        for i in range(n):
            if pre == 0:
                pre = 1

            if suff == 0:
                suff = 1

            pre *= arr[i]

            suff *= arr[n - i - 1]

            ans = max(ans, pre, suff)

        return ans

```

---
*Generated automatically by LeetFeedback Extension*
