# Last updated: 7/12/2026, 6:17:04 PM
class Solution:
    def numberOfSubstrings(self, s: str) -> int:

        n = len(s)
        lastSeen = [-1, -1, -1]
        count = 0
        j = 0

        for i in range(n):
            lastSeen[ord(s[i]) - ord('a')] = i
            count += 1 + min(lastSeen[0], lastSeen[1], lastSeen[2])
    
        return count



        