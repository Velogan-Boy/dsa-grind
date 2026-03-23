# Last updated: 3/24/2026, 1:10:27 AM
1class Solution:
2    def removeKdigits(self, num: str, k: int) -> str:
3        stack = []
4        for i in num:
5            while stack and stack[-1] > i and k > 0:
6                k -= 1
7                stack.pop()
8
9            if stack or i is not "0":
10                stack.append(i)
11
12        if k:
13            stack = stack[:-k]
14            
15        return ''.join(stack) or '0'
16        
17