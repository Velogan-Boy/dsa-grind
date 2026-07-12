# Last updated: 7/12/2026, 6:22:00 PM
class Solution:
    def reverseWords(self, s: str) -> str:  
        i,j, ans, n = 0, 0, '', len(s)

        while i < n:
            while i < n and s[i] == ' ': i+=1
            j = i
            while j < n and s[j] != ' ': j+=1

            w = s[i:j]

            if w:
                ans = w + ' ' + ans
                
            i = j

        return ans.strip()



        