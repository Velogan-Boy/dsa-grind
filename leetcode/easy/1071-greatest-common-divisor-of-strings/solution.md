# Greatest Common Divisor of Strings

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Easy
- **URL:** https://leetcode.com/problems/greatest-common-divisor-of-strings/submissions/1989536031/
- **Date:** 2026-04-27

## Solution

```python
from math import gcd

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""

        length = gcd(len(str1), len(str2))

        return str1[:length]
```

---
*Generated automatically by LeetFeedback Extension*
