# Last updated: 5/15/2026, 10:40:05 AM
1class Solution:
2    def minRemoveToMakeValid(self, s: str) -> str:
3        left_count = 0
4        right_count = 0
5        stack = []
6
7        for ch in s:
8            if ch == '(':
9                left_count += 1
10            elif ch == ')':
11                right_count += 1
12
13            if right_count > left_count:
14                right_count -= 1
15            else:
16                stack.append(ch)
17
18        result = ""
19
20        while stack:
21            current_char = stack.pop()
22            if left_count > right_count and current_char == '(':
23                left_count -= 1
24            else:
25                result += current_char
26
27        # Reverse the result string
28        return result[::-1]