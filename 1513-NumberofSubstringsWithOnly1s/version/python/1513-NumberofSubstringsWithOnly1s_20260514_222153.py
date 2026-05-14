# Last updated: 5/14/2026, 10:21:53 PM
1class Solution(object):
2    def numSub(self, s):
3        cnt = 0
4        total = 0
5        mod = 1000000007
6        for a in s:
7            if a == '1':
8                cnt += 1
9            else:
10                cnt = 0
11            total = (total + cnt) % mod
12        return total