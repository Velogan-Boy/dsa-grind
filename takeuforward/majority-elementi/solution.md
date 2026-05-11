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

        hashMap = defaultdict(int)
        n = len(nums)

        for num in nums:
            hashMap[num]+=1

            if hashMap[num] > n // 2: 
                return num
        
     

            
        
```

---
*Generated automatically by LeetFeedback Extension*
