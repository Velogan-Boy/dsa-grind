# Last updated: 5/9/2026, 12:00:19 AM
1class Solution:
2    def isValid(self, s: str) -> bool:
3        bracketMap = {")": "(", "]": "[", "}": "{"}
4        stack = []
5
6        for c in s:
7            if c not in bracketMap:
8                stack.append(c)
9                continue
10
11            if not stack or stack[-1] != bracketMap[c]:
12                return False
13                
14            stack.pop()
15
16        return not stack
17