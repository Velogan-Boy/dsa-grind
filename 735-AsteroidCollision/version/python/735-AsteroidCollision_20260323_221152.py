# Last updated: 3/23/2026, 10:11:52 PM
1class Solution:
2    def asteroidCollision(self, asteroids):
3        
4        n = len(asteroids)
5        st = []
6        
7        for i in range(n):
8            if asteroids[i] > 0:
9                st.append(asteroids[i])
10            else:
11                while (st and st[-1] > 0 and 
12                       st[-1] < abs(asteroids[i])):
13                    st.pop()
14                
15                if st and st[-1] == abs(asteroids[i]):
16                    st.pop()
17                
18                elif not st or st[-1] < 0:
19                    st.append(asteroids[i])
20        
21        return st