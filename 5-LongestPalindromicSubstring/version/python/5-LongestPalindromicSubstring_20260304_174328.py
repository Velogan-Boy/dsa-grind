# Last updated: 3/4/2026, 5:43:28 PM
1class Solution:
2    def longestPalindrome(self, s: str) -> str:
3        if len(s) <= 1:
4            return s
5
6        def expand_from_center(left, right):
7            while left >= 0 and right < len(s) and s[left] == s[right]:
8                left -= 1
9                right += 1
10            return s[left + 1:right]
11
12        max_str = s[0]
13
14        for i in range(len(s) - 1):
15            odd = expand_from_center(i, i)
16            even = expand_from_center(i, i + 1)
17
18            if len(odd) > len(max_str):
19                max_str = odd
20            if len(even) > len(max_str):
21                max_str = even
22
23        return max_str