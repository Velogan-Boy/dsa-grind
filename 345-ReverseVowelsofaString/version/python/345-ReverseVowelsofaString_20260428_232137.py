# Last updated: 4/28/2026, 11:21:37 PM
1class Solution:
2    def reverseVowels(self, s: str) -> str:
3        s = list(s)
4        vowels = set('aeiouAEIOU')
5        i, j = 0, len(s) - 1
6
7        while i < j:
8            if s[i] not in vowels:
9                i += 1
10            elif s[j] not in vowels:
11                j -= 1
12            else:
13                s[i], s[j] = s[j], s[i]
14                i += 1
15                j -= 1
16        
17        return ''.join(s)