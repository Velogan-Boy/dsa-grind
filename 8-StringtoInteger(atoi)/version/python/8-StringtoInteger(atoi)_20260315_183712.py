# Last updated: 3/15/2026, 6:37:12 PM
1class Solution:
2    def myAtoi(self, s: str) -> int:
3
4        def helper(s, i, started, sign, nums):
5
6            if len(s) == i: return sign * nums
7
8            c = s[i]
9
10            if not started:
11                if c == ' ':
12                    return helper(s, i + 1, False, sign, nums)
13
14                if c in '+-':
15                    sign = -1 if c == '-' else 1
16                    return helper(s, i + 1, True, sign, nums)
17                
18                if c.isdigit():
19                    nums = int(c)
20                    return helper(s, i + 1, True, sign, nums)
21
22            else:
23                if c.isdigit():
24                    nums = (nums * 10) + int(c)
25                    return helper(s, i + 1, True, sign, nums)
26
27                else:
28                    return sign * nums
29                
30        ans = helper(s, 0, False, 1, 0)
31
32        if not ans: return 0
33
34        if ans < -2**31:
35            return -2**31
36        if ans > 2**31 - 1:
37            return 2**31 - 1
38        
39        return ans
40        