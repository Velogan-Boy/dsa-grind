# Last updated: 7/12/2026, 6:16:26 PM
class Solution:
    def countGoodNumbers(self, n: int) -> int:

        def myPow(x, n, mod):
            result = 1
            x = x % mod

            while n > 0:
                if n % 2 == 1:
                    result = (result * x) % mod
                x = (x * x) % mod
                n //= 2

            return result

        
        MODULO = 10**9 + 7

        return ( myPow(5, math.ceil(n / 2),MODULO) * myPow(4, n // 2,MODULO) ) % MODULO
        