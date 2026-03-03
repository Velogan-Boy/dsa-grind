# Last updated: 3/3/2026, 4:52:42 PM
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
11            if not s[r].isalnum(): 
12                r-=1
13                continue
14            if s[l].lower() != s[r].lower(): return False
15
16            l+=1
17            r-=1
18        
19
20        return True
21
22        