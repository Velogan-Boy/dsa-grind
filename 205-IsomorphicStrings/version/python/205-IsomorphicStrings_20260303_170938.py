# Last updated: 3/3/2026, 5:09:38 PM
1class Solution:
2    def isIsomorphic(self, s: str, t: str) -> bool:
3        char_index_s = {}
4        char_index_t = {}
5
6        for i in range(len(s)):
7            if s[i] not in char_index_s:
8                char_index_s[s[i]] = i
9
10            if t[i] not in char_index_t:
11                char_index_t[t[i]] = i
12            
13            if char_index_s[s[i]] != char_index_t[t[i]]:
14                return False
15
16        return True