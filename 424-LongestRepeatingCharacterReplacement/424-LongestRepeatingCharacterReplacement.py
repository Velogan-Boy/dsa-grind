# Last updated: 7/12/2026, 6:19:45 PM
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        maxLength = 0
        l,r = 0, 0
        hm = {}
        maxF = 0

        while r < n:
            hm[s[r]] = hm.get(s[r], 0) + 1
            maxF = max(maxF, hm[s[r]])

            if r - l + 1 - maxF > k:
                hm[s[l]] = hm[s[l]] - 1
                l+=1
            
            maxLength = max(r - l + 1, maxLength)
            r+=1

        return maxLength





                

