# Last updated: 3/31/2026, 3:46:45 PM
1class Solution:
2    def checkValidString(self, s: str) -> bool:
3        leftMin, leftMax = 0, 0
4
5        for c in s:
6            if c == "(":
7                leftMin, leftMax = leftMin + 1, leftMax + 1
8            elif c == ")":
9                leftMin, leftMax = leftMin - 1, leftMax - 1
10            else:
11                leftMin, leftMax = leftMin - 1, leftMax + 1
12            if leftMax < 0:
13                return False
14            if leftMin < 0:  # required because -> s = ( * ) (
15                leftMin = 0
16        return leftMin == 0