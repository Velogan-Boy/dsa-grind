# Last updated: 3/4/2026, 5:16:43 PM
1class Solution:
2    def myAtoi(self, s: str) -> int:
3        ans = ''
4        isPos = True
5        started = False
6
7        for c in s:
8            if c == " " and not started:
9                continue
10
11            if c in "+-" and not started:
12                started = True
13                if c == "-":
14                    isPos = False
15                continue
16
17            if c.isdigit():
18                started = True
19                ans += c
20            else:
21                break
22
23        if ans == '':
24            return 0
25
26        ans = int(ans)
27        if not isPos:
28            ans = -ans
29
30        if ans < -2**31:
31            return -2**31
32        if ans > 2**31 - 1:
33            return 2**31 - 1
34
35        return ans