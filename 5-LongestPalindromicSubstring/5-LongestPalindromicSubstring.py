# Last updated: 7/12/2026, 6:26:09 PM
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        maxL = 0
        ans = ""

        for i in range(n):
            i1, j1 = self.expandFromCenter(s, i, i + 1)
            i2, j2 = self.expandFromCenter(s, i, i)

            len1 = j1 - i1 + 1
            len2 = j2 - i2 + 1

            if len1 > maxL:
                maxL = len1
                ans = s[i1:j1+1]
            
            if len2 > maxL:
                maxL = len2
                ans = s[i2:j2+1]
            
        return ans


        
    def expandFromCenter(self,s, i, j):
        n = len(s)

        while i >= 0 and j < n and s[i] == s[j]:
            i-=1
            j+=1

        return [i + 1, j - 1]
        


        
        
