# Last updated: 3/3/2026, 3:53:42 PM
1class Solution:
2    def reverseWords(self, s: str) -> str:  
3        i,j, ans, n = 0, 0, '', len(s)
4
5        while i < n:
6            while i < n and s[i] == ' ': i+=1
7            j = i
8            while j < n and s[j] != ' ': j+=1
9
10            w = s[i:j]
11            ans = w + ' ' + ans   
12            i = j
13
14        return ans.strip()
15
16
17
18        