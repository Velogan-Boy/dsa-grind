# Last updated: 2/28/2026, 10:14:28 PM
class Solution:
    def mergeCharacters(self, s: str, k: int) -> str:
        for i in range(len(s)):
            if s[i] == '-': continue
            
            # back
            j = i - 1
            close = k
            while j >= 0 and close != 0:
                if s[j] == '-':
                    j-=1
                    continue

                if s[i] == s[j]:
                    s = s[:i] + '-' + s[i + 1:]
                else:
                    close -=1

                j -=1

            # front
            j = i + 1
            close = k
            while j < len(s) and close != 0:
                if s[j] == '-': 
                    j+=1
                    continue
                    
                if s[i] == s[j]:
                    s = s[:j] + '-' + s[j+1:]
                else:   
                    close-=1
                    
                j+=1

        ans = ''
        for i in range(len(s)):
            if s[i] != '-':
                ans += s[i]

        return ans
    
        