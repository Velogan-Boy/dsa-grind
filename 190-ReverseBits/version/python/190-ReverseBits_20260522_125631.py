# Last updated: 5/22/2026, 12:56:31 PM
1class Solution:
2    def reverseBits(self, n: int) -> int:
3
4        res = 0
5
6        for i in range(32):
7            bit = (n >> i) & 1
8
9            res = (res << 1) | bit
10
11        return res
12
13       
14        