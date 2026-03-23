# Last updated: 3/24/2026, 12:44:19 AM
1class Solution:
2    def asteroidCollision(self, asteroids):
3    
4        n = len(asteroids)
5        stack = []
6        
7        for a in asteroids:
8            while stack and a < 0 and stack[-1] > 0:
9                diff = a + stack[-1]
10
11                if diff < 0:
12                    stack.pop()
13                elif diff > 0:
14                    a = 0
15                else:
16                    stack.pop()
17                    a = 0
18
19            if a: stack.append(a)
20
21        return stack
22