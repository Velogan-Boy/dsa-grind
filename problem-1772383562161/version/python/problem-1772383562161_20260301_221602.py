# Last updated: 3/1/2026, 10:16:02 PM
1class Solution:
2    def trimTrailingVowels(self, s: str) -> str:
3        hashSet = set(('a','e','i','o','u'))
4
5        i = len(s) - 1
6
7        while i >= 0 and s[i] in hashSet:
8            s = s[:i] + '-' + s[i+1:]
9            i-=1
10
11        ans = ''
12
13        for ch in s:
14            if ch != '-': ans += ch
15
16        return ans
17                
18        