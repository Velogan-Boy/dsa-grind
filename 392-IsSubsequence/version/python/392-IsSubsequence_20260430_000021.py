# Last updated: 4/30/2026, 12:00:21 AM
1class Solution:
2    def isSubsequence(self, s: str, t: str) -> bool:
3
4        if not s: return True
5        if len(s) > len(t): return False
6
7        i = 0
8
9        for j in range(len(t)):
10            if s[i] == t[j]:
11                i+=1
12            
13            if i == len(s): return True
14        
15        return False
16        