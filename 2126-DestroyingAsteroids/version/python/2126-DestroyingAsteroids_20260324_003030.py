# Last updated: 3/24/2026, 12:30:30 AM
1class Solution(object):
2    def asteroidsDestroyed(self, mass, asteroids):
3        asteroids.sort()
4        temp = mass
5        for a in asteroids:
6            if a <= temp:
7                temp += a
8            else:
9                return False
10        return True