# Last updated: 3/21/2026, 11:36:42 PM
1class Solution:
2    def isPowerOfTwo(self, n: int) -> bool:
3        if n == 0: return False
4        return n & (n - 1) == 0
5        