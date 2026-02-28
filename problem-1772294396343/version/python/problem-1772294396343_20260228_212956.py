# Last updated: 2/28/2026, 9:29:56 PM
1class Solution:
2    def sumOfNumbers(self, l: int, r: int, k: int) -> int:
3 
4        MOD = 10**9 + 7
5        
6        n = r - l + 1
7        
8       
9        S = n * (l + r) // 2
10        S %= MOD
11        
12      
13        pow_n = pow(n, k - 1, MOD)
14        
15     
16        pow_10 = pow(10, k, MOD)
17        geo = (pow_10 - 1) * pow(9, MOD - 2, MOD) % MOD
18        
19        ans = pow_n * S % MOD
20        ans = ans * geo % MOD
21        
22        return ans