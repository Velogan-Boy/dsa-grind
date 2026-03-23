# Asteroid Collision

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/asteroid-collision/submissions/1956916317/
- **Date:** 2026-03-23

## Solution

```python
class Solution:
    def asteroidCollision(self, asteroids):
        
        n = len(asteroids)
        st = []
        
        for i in range(n):
            if asteroids[i] > 0:
                st.append(asteroids[i])
            else:
                while (st and st[-1] > 0 and 
                       st[-1] < abs(asteroids[i])):
                    st.pop()
                
                if st and st[-1] == abs(asteroids[i]):
                    st.pop()
                
                elif not st or st[-1] < 0:
                    st.append(asteroids[i])
        
        return st
```

---
*Generated automatically by LeetFeedback Extension*
