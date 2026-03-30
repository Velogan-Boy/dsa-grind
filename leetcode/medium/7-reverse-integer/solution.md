# Reverse Integer

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/reverse-integer/submissions/1964158465/
- **Date:** 2026-03-30

## Solution

```python
class Solution:
    def reverse(self, x: int) -> int:

        MIN = -2147483648  
        MAX = 2147483647  

        res = 0
        while x:
            digit = int(math.fmod(x, 10)) 
            x = int(x / 10)  

            if res > MAX // 10 or (res == MAX // 10 and digit > MAX % 10):
                return 0
            if res < MIN // 10 or (res == MIN // 10 and digit < MIN % 10):
                return 0
            res = (res * 10) + digit

        return res

```

---
*Generated automatically by LeetFeedback Extension*
