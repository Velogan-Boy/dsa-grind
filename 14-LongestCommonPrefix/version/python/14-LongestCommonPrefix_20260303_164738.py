# Last updated: 3/3/2026, 4:47:38 PM
1class Solution:
2    def longestCommonPrefix(self, strs: List[str]) -> str:
3        pref = strs[0]
4        pref_len = len(pref)
5
6        for s in strs[1:]:
7            while pref != s[0:pref_len]:
8                pref_len -= 1
9                if pref_len == 0:
10                    return ""
11                
12                pref = pref[0:pref_len]
13        
14        return pref