# Last updated: 3/31/2026, 1:19:26 PM
1class Solution:
2    def matchPlayersAndTrainers(self, g: List[int], s: List[int]) -> int:
3
4        g.sort()
5        s.sort()
6
7        m = len(g)
8        n = len(s)
9
10        l,r = 0, 0
11
12        while l < m and r < n:
13            if g[l] <= s[r]:
14                l+=1
15            r+=1
16            
17        return l 
18
19
20            
21        