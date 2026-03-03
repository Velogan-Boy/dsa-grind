# Last updated: 3/3/2026, 2:53:57 PM
1class Solution:
2    def removeOuterParentheses(self, s: str) -> str:
3        ans = ""
4
5        state = 0
6        i = 0
7    
8        while i < len(s):
9            if state == 0:
10                state = 1
11                i+=1
12                continue
13
14            if s[i] == '(':
15                state +=1
16            else:
17                state -= 1
18
19            if state != 0:
20                ans += s[i]
21            
22            i+=1
23
24        return ans
25
26
27        
28
29            
30
31
32            
33            
34                
35
36        return ans
37
38            
39
40            
41
42        