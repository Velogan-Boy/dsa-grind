# Last updated: 7/12/2026, 6:17:29 PM
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans = ""

        state = 0
        i = 0
    
        while i < len(s):
            if state == 0:
                state = 1
                i+=1
                continue

            if s[i] == '(':
                state +=1
            else:
                state -= 1

            if state != 0:
                ans += s[i]
            
            i+=1

        return ans


        

            


            
            
                

        return ans

            

            

        