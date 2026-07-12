# Last updated: 7/12/2026, 6:16:13 PM
class Solution(object):
    def asteroidsDestroyed(self, mass, asteroids):
        asteroids.sort()
        temp = mass
        for a in asteroids:
            if a <= temp:
                temp += a
            else:
                return False
        return True