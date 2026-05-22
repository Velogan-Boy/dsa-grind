# Last updated: 5/22/2026, 12:59:47 PM
1class Solution:
2    def reverseBits(self, n: int) -> int:
3
4        res = 0
5
6        for i in range(32):
7            bit = (n >> i) & 1
8            res += (bit << (31 - i))
9
10        return res
11
12       
13        