# Last updated: 7/12/2026, 6:25:46 PM
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pref = strs[0]
        res = ""

        for i in range(len(pref)):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res
                
            res += s[i]

        return res
        
