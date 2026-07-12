# Last updated: 7/12/2026, 6:19:35 PM
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        m = len(g)
        n = len(s)

        l,r = 0, 0

        while l < m and r < n:
            if g[l] <= s[r]:
                l+=1
            
            r+=1
            
        return l 


            