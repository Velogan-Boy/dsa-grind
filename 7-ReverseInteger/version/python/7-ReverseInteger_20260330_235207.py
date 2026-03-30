# Last updated: 3/30/2026, 11:52:07 PM
1class Solution:
2    def reverse(self, x: int) -> int:
3
4        MIN = -2147483648  
5        MAX = 2147483647  
6
7        res = 0
8        while x:
9            digit = int(math.fmod(x, 10)) 
10            x = int(x / 10)  
11
12            if res > MAX // 10 or (res == MAX // 10 and digit > MAX % 10):
13                return 0
14            if res < MIN // 10 or (res == MIN // 10 and digit < MIN % 10):
15                return 0
16            res = (res * 10) + digit
17
18        return res
19