# Last updated: 6/4/2026, 12:47:12 AM
1class Solution:
2    def isPalindrome(self, s: str) -> bool:
3
4        l = 0
5        r = len(s) - 1
6
7        while l < r:
8            if not s[l].isalnum(): 
9                l+=1
10                continue
11
12            if not s[r].isalnum(): 
13                r-=1
14                continue
15                
16            if s[l].lower() != s[r].lower(): return False
17
18            l+=1
19            r-=1
20        
21
22        return True
23
24        