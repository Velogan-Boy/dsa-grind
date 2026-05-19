# Last updated: 5/19/2026, 8:13:43 PM
1class Solution:
2    def isValid(self, s: str) -> bool:
3
4        hashMap = {'}': '{', ')': '(', ']':'['}
5        stack = []
6
7        for ch in s:
8            if stack and ch in hashMap and stack[-1] == hashMap[ch]:
9                stack.pop()
10            else:
11                stack.append(ch)
12
13        return not stack
14            
15
16        