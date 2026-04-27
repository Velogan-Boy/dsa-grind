# Last updated: 4/27/2026, 9:40:55 PM
1from math import gcd
2
3class Solution:
4    def gcdOfStrings(self, str1: str, str2: str) -> str:
5        if str1 + str2 != str2 + str1:
6            return ""
7
8        length = gcd(len(str1), len(str2))
9
10        return str1[:length]