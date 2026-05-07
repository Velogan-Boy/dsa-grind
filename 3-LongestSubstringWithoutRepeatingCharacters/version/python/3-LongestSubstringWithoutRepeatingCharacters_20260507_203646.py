# Last updated: 5/7/2026, 8:36:46 PM
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
15            
16
17        return ans
18
19            
20
21        