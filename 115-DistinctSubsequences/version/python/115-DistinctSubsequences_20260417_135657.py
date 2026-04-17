# Last updated: 4/17/2026, 1:56:57 PM
1class Solution:
2    def numDistinct(self, s: str, t: str) -> int:
3        m,n = len(s), len(t)
4
5        prev = [0] * (n + 1)
6
7        prev[n] = 1
8
9        for i in range(m - 1, -1, -1):
10            curr = [0] * (n + 1)
11            curr[n] = 1
12
13            for j in range(n - 1, -1, -1):
14                if s[i] == t[j]:
15                   curr[j] = prev[j + 1] + prev[j]
16                else:
17                   curr[j] = prev[j]
18
19            prev = curr
20
21        
22        return prev[0]