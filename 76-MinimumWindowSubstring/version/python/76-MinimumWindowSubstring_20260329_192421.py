# Last updated: 3/29/2026, 7:24:21 PM
1class Solution:
2    def minWindow(self, s: str, t: str) -> str:
3        n = len(s)
4
5        hm = [0] * 256
6        for c in t:
7            hm[ord(c)] += 1
8
9        l = 0
10        count = 0
11        minLength = inf
12        start = -1
13
14        for r in range(n):
15            if hm[ord(s[r])] > 0:
16                count += 1
17            
18            hm[ord(s[r])] -= 1
19
20            while count == len(t):
21                if r - l + 1 < minLength:
22                    minLength = r - l + 1
23                    start = l
24                
25                hm[ord(s[l])] += 1
26                if hm[ord(s[l])] > 0:
27                    count -= 1
28                
29                l += 1
30
31        return "" if start == -1 else s[start:start + minLength]