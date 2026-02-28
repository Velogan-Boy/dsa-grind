# Last updated: 2/28/2026, 8:45:11 PM
1class Solution:
2    def mergeCharacters(self, s: str, k: int) -> str:
3        for i in range(len(s)):
4            if s[i] == '-': continue
5            
6            # back
7            j = i - 1
8            close = k
9            while j >= 0 and close != 0:
10                if s[j] == '-':
11                    j-=1
12                    continue
13
14                if s[i] == s[j]:
15                    s = s[:i] + '-' + s[i + 1:]
16                else:
17                    close -=1
18
19                j -=1
20
21            # front
22            j = i + 1
23            close = k
24            while j < len(s) and close != 0:
25                if s[j] == '-': 
26                    j+=1
27                    continue
28                    
29                if s[i] == s[j]:
30                    s = s[:j] + '-' + s[j+1:]
31                else:   
32                    close-=1
33                    
34                j+=1
35
36        ans = ''
37        for i in range(len(s)):
38            if s[i] != '-':
39                ans += s[i]
40
41        return ans
42    
43        