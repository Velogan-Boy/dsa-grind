# Last updated: 3/24/2026, 10:09:52 PM
1class Solution:
2    def lengthOfLongestSubstring(self, s):
3        n = len(s)
4        maxLength = 0
5
6        l = 0
7        r = 0
8        hm = {}
9
10        while r < n:
11            if s[r] in hm:
12                l = max(hm[s[r]] + 1, l)
13            
14            hm[s[r]] = r
15            maxLength = max(r - l + 1, maxLength)
16            r+=1
17
18        return maxLength
19
20
21        
22
23
24
25