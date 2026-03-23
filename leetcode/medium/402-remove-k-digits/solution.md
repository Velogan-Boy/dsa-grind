# Remove K Digits

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/remove-k-digits/submissions/1957105968/
- **Date:** 2026-03-23

## Solution

```python
class Solution:
    def removeKdigits(self, nums: str, k: int) -> str:
        st = []
        
        for digit in nums:
            while st and k > 0 and st[-1] > digit:
                st.pop() 
                k -= 1 
            
            st.append(digit)
        
        while st and k > 0:
            st.pop() 
            k -= 1 
        
        if not st:
            return "0"
        
        res = ""
        
        while st:
            res += st.pop()
        
        res = res.rstrip('0')
        
        res = res[::-1]
        
        if not res:
            return "0"
        
        return res

```

---
*Generated automatically by LeetFeedback Extension*
