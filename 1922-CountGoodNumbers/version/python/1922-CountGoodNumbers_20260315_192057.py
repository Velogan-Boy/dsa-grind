# Last updated: 3/15/2026, 7:20:57 PM
1class Solution:
2    def countGoodNumbers(self, n: int) -> int:
3
4        def myPow(x, n, mod):
5            result = 1
6            x = x % mod
7
8            while n > 0:
9                if n % 2 == 1:
10                    result = (result * x) % mod
11                x = (x * x) % mod
12                n //= 2
13
14            return result
15
16        
17        MODULO = 10**9 + 7
18
19        return ( myPow(5, math.ceil(n / 2),MODULO) * myPow(4, n // 2,MODULO) ) % MODULO
20        