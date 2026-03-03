# Last updated: 3/3/2026, 4:31:26 PM
1class Solution:
2    def largestOddNumber(self, num: str) -> str:
3        j = len(num) - 1
4
5        while j >= 0:
6            if int(num[j]) % 2 == 1:
7                break
8            j-=1
9        
10        return num[:j+1]
11
12
13
14        