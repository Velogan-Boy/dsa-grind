# Last updated: 3/24/2026, 1:09:24 AM
1class Solution:
2    def removeKdigits(self, num: str, k: int) -> str:
3        stack = []
4        for i in num:
5            while stack and stack[-1] > i and k > 0:
6                k -= 1
7                stack.pop()
8            if stack or i is not "0":
9                stack.append(i)
10        if k:
11            stack = stack[:-k]
12        return ''.join(stack) or '0'
13        
14