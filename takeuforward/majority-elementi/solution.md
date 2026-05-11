# Majority Element-I

## Problem Information
- **Platform:** Takeuforward
- **Difficulty:** Unknown
- **URL:** https://takeuforward.org/plus/dsa/problems/majority-element-i
- **Date:** 2026-05-11

## Solution

```python
import math
from collections import defaultdict

class Solution:
    def majorityElement(self, nums):

        cnt = 1
        element = nums[0]

        for i in range(1, len(nums)):
            if nums[i] == element:
                cnt+=1
            else:
                if cnt > 0: cnt -= 1
                else:
                    element = nums[i]
                    cnt = 1
        
        return element
     

            
        
```

---
*Generated automatically by LeetFeedback Extension*
