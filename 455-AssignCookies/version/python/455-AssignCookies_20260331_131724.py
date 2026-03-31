# Last updated: 3/31/2026, 1:17:24 PM
1class Solution:
2    def findContentChildren(self, g: List[int], s: List[int]) -> int:
3        g.sort()
4        s.sort()
5
6        m = len(g)
7        n = len(s)
8
9        l,r = 0, 0
10
11        while l < m and r < n:
12            if g[l] <= s[r]:
13                l+=1
14            
15            r+=1
16            
17        return l 
18
19
20            