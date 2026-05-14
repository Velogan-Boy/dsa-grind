# Last updated: 5/14/2026, 10:21:16 PM
1class Solution:
2    def numSub(self, s: str) -> int:
3        MOD = 10**9 + 7
4        i = 0
5        n = len(s)
6        cnt = 0
7
8        while i < n:
9            # Skip all '0's
10            while i < n and s[i] == '0':
11                i += 1
12
13            j = i
14            subs = 1
15
16            while j < n and s[j] == '1':
17                cnt = (cnt + subs) % MOD
18                subs += 1
19                j += 1
20
21            i = j
22
23        return cnt