# Last updated: 5/29/2026, 10:46:52 PM
1class Solution:
2    def lengthOfLongestSubstring(self, s: str) -> int:
3        i, j = 0, 0
4        n = len(s)
5        hashMap = {}
6        ans = 0
7
8        while j < n:
9            if s[j] in hashMap:
10                i = max(hashMap[s[j]] + 1, i)
11            
12            hashMap[s[j]] = j
13            ans = max(ans, j - i + 1)
14            j+=1
15
16        return ans
17
18            
19
20
21        