# Lemonade Change

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Easy
- **URL:** https://leetcode.com/problems/lemonade-change/submissions/1964728219/
- **Date:** 2026-03-31

## Solution

```python
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0
        ten = 0

        for i in range(len(bills)):
            if bills[i] == 5:
                five += 1
            elif bills[i] == 10:
                if five > 0:
                    five -= 1
                    ten += 1
                else:
                    return False
            elif bills[i] == 20:
                if five > 0 and ten > 0:
                    five -= 1
                    ten -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
                    
        return True
```

---
*Generated automatically by LeetFeedback Extension*
