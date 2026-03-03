# Last updated: 3/3/2026, 3:53:24 PM
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
11
12            if w:
13                ans = w + ' ' + ans
14                
15            i = j
16
17        return ans.strip()
18
19
20
21        