# Last updated: 5/29/2026, 10:32:10 PM
1class Solution:
2    def lengthOfLongestSubstring(self, s: str) -> int:
3        i, j = 0, 0
4        hashMap = {}
5        ans = 0
6
7        while j < len(s):
8            if s[j] in hashMap:
9                i = max(i, hashMap[s[j]] + 1)
10
11            hashMap[s[j]] = j
12            ans = max(ans, j - i + 1)
13            j+=1
14
15        return ans
16
17            
18
19        