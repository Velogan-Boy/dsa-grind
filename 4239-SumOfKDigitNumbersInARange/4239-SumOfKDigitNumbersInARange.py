# Last updated: 2/28/2026, 10:14:27 PM
class Solution:
    def sumOfNumbers(self, l: int, r: int, k: int) -> int:
 
        MOD = 10**9 + 7
        
        n = r - l + 1
        
       
        S = n * (l + r) // 2
        S %= MOD
        
      
        pow_n = pow(n, k - 1, MOD)
        
     
        pow_10 = pow(10, k, MOD)
        geo = (pow_10 - 1) * pow(9, MOD - 2, MOD) % MOD
        
        ans = pow_n * S % MOD
        ans = ans * geo % MOD
        
        return ans