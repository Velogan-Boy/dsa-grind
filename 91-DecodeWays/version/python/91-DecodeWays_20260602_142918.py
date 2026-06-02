# Last updated: 6/2/2026, 2:29:18 PM
1class Solution:
2    def numDecodings(self, s: str) -> int:
3        
4        n = len(s)
5
6        @cache
7        def dfs(i):
8            if i == n: return 1
9
10            l,r = 0, 0
11            if s[i] != '0':
12                l = dfs(i + 1)
13            
14            if s[i] != '0' and i != n - 1 and int(s[i] + s[i + 1]) <= 26:
15                r = dfs(i + 2)
16            
17            return l + r
18
19        return dfs(0)
20
21
22
23        