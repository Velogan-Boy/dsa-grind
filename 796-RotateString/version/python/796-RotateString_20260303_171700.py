# Last updated: 3/3/2026, 5:17:00 PM
1class Solution:
2    def rotateString(self, s: str, goal: str) -> bool:
3        if len(s) != len(goal):
4            return False
5        return goal in s + s