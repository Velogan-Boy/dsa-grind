# Last updated: 5/31/2026, 10:58:37 PM
1class Solution:
2    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
3
4        if len(s1) + len(s2) != len(s3):
5            return False
6
7        @cache
8        def dfs(i, j):
9            if i == len(s1) and j == len(s2):
10                return True
11
12            k = i + j
13
14            if i < len(s1) and s1[i] == s3[k]:
15                if dfs(i + 1, j):
16                    return True
17
18            if j < len(s2) and s2[j] == s3[k]:
19                if dfs(i, j + 1):
20                    return True
21
22            return False
23
24        return dfs(0, 0)