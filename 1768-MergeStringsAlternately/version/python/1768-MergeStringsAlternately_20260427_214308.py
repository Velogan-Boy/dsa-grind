# Last updated: 4/27/2026, 9:43:08 PM
1class Solution:
2    def mergeAlternately(self, word1: str, word2: str) -> str:
3        i, j = 0, 0
4        m, n = len(word1), len(word2)
5        res = []
6
7        while i < m and j < n:
8            res.append(word1[i])
9            res.append(word2[j])
10            i += 1
11            j += 1
12
13        if i < m:
14            res.append(word1[i:])
15        if j < n:
16            res.append(word2[j:])
17
18        return "".join(res)