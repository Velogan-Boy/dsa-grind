# Last updated: 4/28/2026, 11:28:00 PM
1class Solution:
2    def reverseWords(self, s: str) -> str:  
3        i,j, ans, n = 0, 0, '', len(s)
4
5        while i < n:
6            while i < n and s[i] == ' ': i+=1
7            if i >= n: break
8
9            j = i + 1
10            while j < n and s[j] != ' ': j+=1
11
12            if ans:
13                ans = s[i:j] + ' ' + ans
14            else:
15                ans = s[i:j]
16
17            i = j + 1
18
19        return ans
20
21
22
23        