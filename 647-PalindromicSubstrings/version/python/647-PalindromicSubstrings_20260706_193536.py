# Last updated: 7/6/2026, 7:35:36 PM
1class Solution:
2    def countSubstrings(self, s: str) -> int:
3        n = len(s) 
4
5        if not s or len(s) == 0: return 0
6
7        if len(s) == 1: return 1
8        
9        ans = 0
10        for i in range(n):
11            ans += self.expandFromCenter(s,i, i)
12            ans += self.expandFromCenter(s,i, i + 1)
13        
14        return ans
15
16
17
18
19    def expandFromCenter(self, s, i, j):
20        n = len(s)
21        count = 0
22
23        while i >= 0 and j < n and s[i] == s[j]:
24            i-=1
25            j+=1
26            count += 1
27        
28        return count
29        
30
31        