# Last updated: 4/27/2026, 9:28:52 PM
1class Solution:
2    def mergeAlternately(self, word1: str, word2: str) -> str:
3
4        i, j = 0, 0
5        m,n = len(word1), len(word2)
6        res = ""
7
8        while i < m and j < n:
9            res += word1[i]
10            res += word2[j]
11
12            i+=1
13            j+=1
14        
15        if i < m:
16            res += word1[i:]
17        
18        if j < n:
19            res += word2[j:]
20
21        return res
22
23
24        