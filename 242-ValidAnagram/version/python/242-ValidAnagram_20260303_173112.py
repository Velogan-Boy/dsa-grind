# Last updated: 3/3/2026, 5:31:12 PM
1class Solution:
2    def isAnagram(self, s: str, t: str) -> bool:  
3        if len(s) != len(t):
4            return False
5
6        counter = {}
7
8        for char in s:
9            counter[char] = counter.get(char, 0) + 1
10
11        for char in t:
12            if char not in counter or counter[char] == 0:
13                return False
14            counter[char] -= 1
15
16        return True