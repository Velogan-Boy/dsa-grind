# Last updated: 4/15/2026, 8:18:30 PM
1class Solution:
2    def minDistance(self, A: str, B: str) -> int:
3        m, n = len(A), len(B)
4
5        prev = [0] * (n + 1)
6
7        for i in range(1, m + 1):
8            curr = [0] * (n + 1)
9            for j in range(1, n + 1):
10                if A[i - 1] == B[j - 1]:
11                    curr[j] = 1 + prev[j - 1]
12                else:
13                    curr[j] = max(prev[j], curr[j - 1])
14            prev = curr
15
16        lcs = prev[n]
17        return (m - lcs) + (n - lcs)