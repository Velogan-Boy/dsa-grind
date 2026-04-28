# Last updated: 4/28/2026, 11:21:16 PM
1class Solution:
2    def reverseVowels(self, s: str) -> str:
3        s = list(s)
4        i, j = 0, len(s) - 1
5
6        while i < j:
7            if s[i] not in 'aeiouAEIOU':
8                i += 1
9            elif s[j] not in 'aeiouAEIOU':
10                j -= 1
11            else:
12                s[i], s[j] = s[j], s[i]
13                i += 1
14                j -= 1
15        
16        return ''.join(s) 