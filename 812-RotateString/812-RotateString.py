# Last updated: 2/27/2026, 5:21:42 PM
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return len(s) == len(goal) and goal in (s + s)