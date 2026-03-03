# Last updated: 3/3/2026, 5:11:59 PM
1class Solution:
2    def isIsomorphic(self, s: str, t: str) -> bool:
3        char_map = {}
4
5        for sc, tc in zip(s, t):
6            if sc in char_map:
7                if char_map[sc] != tc:
8                    return False
9            elif tc in char_map.values():
10                return False
11
12            char_map[sc] = tc
13
14        return True