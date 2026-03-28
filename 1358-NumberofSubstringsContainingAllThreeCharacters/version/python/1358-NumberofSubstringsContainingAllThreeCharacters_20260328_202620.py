# Last updated: 3/28/2026, 8:26:20 PM
1class Solution:
2    def numberOfSubstrings(self, s: str) -> int:
3
4        n = len(s)
5        lastSeen = [-1, -1, -1]
6        count = 0
7        j = 0
8
9        for i in range(n):
10            lastSeen[ord(s[i]) - ord('a')] = i
11            count += 1 + min(lastSeen[0], lastSeen[1], lastSeen[2])
12    
13        return count
14
15
16
17        