# Fizz Buzz

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Easy
- **URL:** https://leetcode.com/problems/fizz-buzz/submissions/2065227852/
- **Date:** 2026-07-12

## Solution

```python
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:

        answer = [""] * n

        for i in range(1,n + 1):
            if i % 3 == 0:
                answer[i - 1] += "Fizz"
            
            if i % 5 == 0:
                answer[i - 1] += "Buzz"

            if i % 3 != 0 and i % 5 != 0:
                answer[i - 1] += str(i)

        return answer
            

            

        
```

---
*Generated automatically by LeetFeedback Extension*
