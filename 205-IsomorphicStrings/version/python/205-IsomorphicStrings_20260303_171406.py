# Last updated: 3/3/2026, 5:14:06 PM
1class Solution:
2    def isIsomorphic(self, s: str, t: str) -> bool:
3        return len(set(s)) == len(set(t)) == len(set(zip(s,t)))