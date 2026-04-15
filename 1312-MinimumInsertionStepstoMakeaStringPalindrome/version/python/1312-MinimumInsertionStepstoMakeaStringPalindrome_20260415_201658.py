# Last updated: 4/15/2026, 8:16:58 PM
1class Solution:
2    def minInsertions(self, s: str) -> int:
3        t = s[::-1]
4        n = len(s)
5
6        prev = [0] * (n + 1)
7
8        for i in range(1, n + 1):
9            curr = [0] * (n + 1)
10            for j in range(1, n + 1):
11                if s[i - 1] == t[j - 1]:
12                    curr[j] = 1 + prev[j - 1]
13                else:
14                    curr[j] = max(prev[j], curr[j - 1])
15            prev = curr
16
17        lps = prev[n]
18        return n - lps