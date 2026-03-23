# Asteroid Collision

## Problem Information
- **Platform:** Leetcode
- **Difficulty:** Medium
- **URL:** https://leetcode.com/problems/asteroid-collision/submissions/1957088285/
- **Date:** 2026-03-23

## Solution

```python
class Solution:
    def asteroidCollision(self, asteroids):
    
        n = len(asteroids)
        stack = []
        
        for a in asteroids:
            while stack and a < 0 and stack[-1] > 0:
                diff = a + stack[-1]

                if diff < 0:
                    stack.pop()
                elif diff > 0:
                    a = 0
                else:
                    stack.pop()
                    a = 0

            if a: stack.append(a)

        return stack

```

---
*Generated automatically by LeetFeedback Extension*
