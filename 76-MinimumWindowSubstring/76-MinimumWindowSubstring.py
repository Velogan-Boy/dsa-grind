# Last updated: 7/12/2026, 6:23:51 PM
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)

        hm = [0] * 256
        for c in t:
            hm[ord(c)] += 1

        l = 0
        count = 0
        minLength = inf
        start = -1

        for r in range(n):
            if hm[ord(s[r])] > 0:
                count += 1
            
            hm[ord(s[r])] -= 1

            while count == len(t):
                if r - l + 1 < minLength:
                    minLength = r - l + 1
                    start = l
                
                hm[ord(s[l])] += 1
                if hm[ord(s[l])] > 0:
                    count -= 1
                
                l += 1

        return "" if start == -1 else s[start:start + minLength]