# Last updated: 5/22/2026, 12:33:50 PM
1class Solution:
2    def hammingWeight(self, n: int) -> int:
3
4        return bin(n).count('1')