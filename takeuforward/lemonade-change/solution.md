# Lemonade Change

## Problem Information
- **Platform:** Takeuforward
- **Difficulty:** Unknown
- **URL:** https://takeuforward.org/plus/dsa/problems/lemonade-change
- **Date:** 2026-05-17

## Solution

```python
class Solution:
    def lemonadeChange(self, bills):
        count_5 = 0
        count_10 = 0

        for bill in bills:
            if bill == 5:
                count_5 += 1
            elif bill == 10:
                if count_5 == 0: return False
                count_5 -= 1
                count_10 += 1
            else:
                if count_10 > 0 and count_5 > 0:
                    count_10 -= 1
                    count_5 -= 1
                elif count_5 >= 3:
                    count_5 -= 3
                else:
                    return False

        return True
                
            

    
```

---
*Generated automatically by LeetFeedback Extension*
