# Last updated: 4/15/2026, 7:11:17 PM
1class Solution:
2    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
3        m,n = len(text1), len(text2)
4
5        prev = [0] * (n + 1) 
6
7        for i in range(1, m + 1):
8            curr = [0] * (n + 1)
9
10            for j in range(1, n + 1):
11                if text1[i - 1] == text2[j - 1]:
12                    curr[j] =  1 + prev[j - 1]
13                else:
14                    curr[j] = max(prev[j], curr[j - 1])
15
16            prev = curr
17
18        return prev[n]
19        