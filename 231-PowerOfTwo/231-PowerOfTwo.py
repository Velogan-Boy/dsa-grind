# Last updated: 7/12/2026, 6:20:56 PM
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0: return False
        return n & (n - 1) == 0
        