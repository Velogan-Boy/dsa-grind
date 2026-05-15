# Last updated: 5/15/2026, 10:50:31 AM
1class Solution:
2    def minAddToMakeValid(self, s: str) -> int:
3        open_c = close_c = 0
4        for c in s:
5            if c == '(':
6                open_c += 1
7            elif c == ')' and open_c > 0:
8                open_c -= 1
9            else:
10                close_c += 1
11        return open_c + close_c