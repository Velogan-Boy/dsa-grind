# Last updated: 7/12/2026, 6:18:56 PM
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s) 

        if not s or len(s) == 0: return 0

        if len(s) == 1: return 1
        
        ans = 0
        for i in range(n):
            ans += self.expandFromCenter(s,i, i)
            ans += self.expandFromCenter(s,i, i + 1)
        
        return ans




    def expandFromCenter(self, s, i, j):
        n = len(s)
        count = 0

        while i >= 0 and j < n and s[i] == s[j]:
            i-=1
            j+=1
            count += 1
        
        return count
        

        