# Last updated: 5/8/2026, 11:07:16 PM
1class Solution:
2    def longestCommonPrefix(self, strs: List[str]) -> str:
3        pref = strs[0]
4        res = ""
5
6        for i in range(len(pref)):
7            for s in strs:
8                if i == len(s) or s[i] != strs[0][i]:
9                    return res
10                
11            res += s[i]
12
13        return res
14        
15