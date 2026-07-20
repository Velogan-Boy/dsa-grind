# Last updated: 7/20/2026, 11:02:41 PM
1class Solution:
2    def lengthOfLongestSubstring(self, s: str) -> int:
3        hm = {}
4        i = 0
5        ans = 0
6
7        for j in range(len(s)):
8            if s[j] in hm:
9                i = max(i, hm[s[j]] + 1)
10
11            hm[s[j]] = j
12            ans = max(ans, j - i + 1)
13
14        return ans