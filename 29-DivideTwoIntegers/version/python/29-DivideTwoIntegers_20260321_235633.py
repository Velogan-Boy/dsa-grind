# Last updated: 3/21/2026, 11:56:33 PM
1class Solution:
2    def divide(self, dividend: int, divisor: int) -> int:
3        if dividend == divisor:
4            return 1
5        if dividend == -2**31 and divisor == -1:
6            return (2**31) - 1 
7        
8        if divisor == 1:
9            return dividend
10        
11        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
12        
13        n, d = abs(dividend), abs(divisor)
14        ans = 0
15
16        while n >= d:
17            p = 0
18            while n >= (d << p):
19                p += 1
20            
21            p -= 1
22            n -= (d << p)
23            ans += (1 << p)
24
25        return min(max(sign * ans, -2**31), 2**31 - 1)