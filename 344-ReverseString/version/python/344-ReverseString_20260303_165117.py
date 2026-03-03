# Last updated: 3/3/2026, 4:51:17 PM
1class Solution:
2    def reverseString(self, s: List[str]) -> None:
3        
4        i = 0
5        j = len(s) - 1
6
7        while i < j:
8            s[i], s[j] = s[j],s[i]
9            i+=1
10            j-=1
11
12        return s
13        