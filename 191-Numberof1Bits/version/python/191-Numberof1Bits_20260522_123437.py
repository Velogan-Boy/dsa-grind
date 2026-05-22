# Last updated: 5/22/2026, 12:34:37 PM
1class Solution:
2    def hammingWeight(self, n: int) -> int:
3
4        count = 0
5        while n:
6            n = n & (n - 1)
7            count+=1
8
9        return count