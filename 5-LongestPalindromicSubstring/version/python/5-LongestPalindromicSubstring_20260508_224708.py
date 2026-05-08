# Last updated: 5/8/2026, 10:47:08 PM
1class Solution:
2    def longestPalindrome(self, s: str) -> str:
3        n = len(s)
4
5        if n <= 1: return s
6
7        def expandFromCenter(l, r):
8            while l >= 0 and r < n and s[l] == s[r]:
9                l-=1
10                r+=1
11            
12            return s[l+1:r]
13
14        maxP = s[0]
15        for i in range(n):
16            odd = expandFromCenter(i,i)
17            even = expandFromCenter(i, i + 1)
18
19            if len(odd) > len(maxP):
20                maxP = odd
21            
22            if len(even) > len(maxP):
23                maxP = even
24            
25        return maxP
26        
27
28
29
30       