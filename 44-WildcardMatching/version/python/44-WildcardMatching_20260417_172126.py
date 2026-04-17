# Last updated: 4/17/2026, 5:21:26 PM
1class Solution:
2    def isAllStars(self, S1, i):
3        for j in range(i + 1):
4            if S1[j] != '*':
5                return False
6        return True
7
8    @cache
9    def wildcardMatchingUtil(self, S1, S2, i, j):
10        if i < 0 and j < 0:
11            return True
12        if i < 0 and j >= 0:
13            return False
14        if j < 0 and i >= 0:
15            return self.isAllStars(S1, i)
16
17        if S1[i] == S2[j] or S1[i] == '?':
18            return self.wildcardMatchingUtil(S1, S2, i - 1, j - 1)
19
20        if S1[i] == '*':
21            return (self.wildcardMatchingUtil(S1, S2, i - 1, j) or
22                    self.wildcardMatchingUtil(S1, S2, i, j - 1))
23                    
24        return False
25
26    def isMatch(self, str, pat):
27        n = len(str)
28        m = len(pat)
29        return self.wildcardMatchingUtil(pat, str, m - 1, n - 1)
30