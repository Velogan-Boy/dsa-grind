# Last updated: 7/3/2026, 11:51:44 PM
1class Solution:
2    def characterReplacement(self, s: str, k: int) -> int:
3        n = len(s)
4        maxLength = 0
5        l,r = 0, 0
6        hm = {}
7        maxF = 0
8
9        while r < n:
10            hm[s[r]] = hm.get(s[r], 0) + 1
11            maxF = max(maxF, hm[s[r]])
12
13            if r - l + 1 - maxF > k:
14                hm[s[l]] = hm[s[l]] - 1
15                l+=1
16            
17            maxLength = max(r - l + 1, maxLength)
18            r+=1
19
20        return maxLength
21
22
23
24
25
26                
27
28