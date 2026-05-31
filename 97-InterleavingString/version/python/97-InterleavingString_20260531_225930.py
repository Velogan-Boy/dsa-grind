# Last updated: 5/31/2026, 10:59:30 PM
1class Solution:
2    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
3
4        if len(s1) + len(s2) != len(s3):
5            return False
6
7        memo = {}
8
9        def dfs(i, j):
10
11            if (i, j) in memo:
12                return memo[(i, j)]
13
14            if i == len(s1) and j == len(s2):
15                return True
16
17            k = i + j
18
19            ans = False
20
21            if i < len(s1) and s1[i] == s3[k]:
22                ans = dfs(i + 1, j)
23
24            if not ans and j < len(s2) and s2[j] == s3[k]:
25                ans = dfs(i, j + 1)
26
27            memo[(i, j)] = ans
28            return ans
29
30        return dfs(0, 0)