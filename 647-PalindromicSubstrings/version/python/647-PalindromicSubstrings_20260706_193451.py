# Last updated: 7/6/2026, 7:34:51 PM
1class Solution:
2    def countSubstrings(self, s: str) -> int:
3        n = len(s)
4
5        ans = 0
6        for i in range(n):
7            ans += self.expandFromCenter(s,i, i)
8            ans += self.expandFromCenter(s,i, i + 1)
9        
10        return ans
11
12
13
14
15    def expandFromCenter(self, s, i, j):
16        n = len(s)
17        count = 0
18
19        while i >= 0 and j < n and s[i] == s[j]:
20            i-=1
21            j+=1
22            count += 1
23        
24        return count
25        
26
27        