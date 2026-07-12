# Last updated: 7/12/2026, 6:26:10 PM
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j = 0, 0
        n = len(s)
        hashMap = {}
        ans = 0

        while j < n:
            if s[j] in hashMap:
                i = max(hashMap[s[j]] + 1, i)
            
            hashMap[s[j]] = j
            ans = max(ans, j - i + 1)
            j+=1

        return ans

            


        