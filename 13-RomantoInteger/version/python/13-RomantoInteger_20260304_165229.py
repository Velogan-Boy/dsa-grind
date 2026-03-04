# Last updated: 3/4/2026, 4:52:29 PM
1class Solution:
2    def romanToInt(self, s: str) -> int:
3        roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
4        
5        res = 0
6        for i in range(len(s)):
7            if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]:
8                res -= roman[s[i]]
9            else:
10                res += roman[s[i]]
11        return res
12