# Last updated: 3/3/2026, 4:32:17 PM
1class Solution:
2    def largestOddNumber(self, num: str) -> str:
3        for i in range(len(num) - 1, -1, -1):
4            if num[i] in "13579":
5                return num[:i+1]
6        return ""