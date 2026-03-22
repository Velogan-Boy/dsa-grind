# Last updated: 3/22/2026, 1:52:55 PM
1class Solution:
2    def minBitFlips(self, start: int, goal: int) -> int:
3
4        n = start ^ goal
5
6        cnt = 0
7        while n != 0:
8            n = n & (n - 1)
9            cnt += 1
10
11        return cnt
12
13        