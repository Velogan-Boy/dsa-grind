# Last updated: 5/15/2026, 10:31:16 AM
1class Solution:
2    def minRemoveToMakeValid(self, s: str) -> str:
3
4        n = len(s)
5        arr = list(s)
6        openParanthesis = 0
7
8        for i in range(n):
9            if arr[i] == '(':
10                openParanthesis += 1
11            elif arr[i] == ')':
12                if openParanthesis == 0:
13                    arr[i] = '*'
14                else:
15                    openParanthesis -= 1
16
17        closeParanthesis = 0
18        for i in range(n - 1, -1, -1):
19            if arr[i] == ')':
20                closeParanthesis += 1
21            elif arr[i] == '(':
22                if closeParanthesis == 0:
23                    arr[i] = '*'
24                else:
25                    closeParanthesis -= 1
26
27        
28        return ''.join(c for c in arr if c != '*')
29
30        