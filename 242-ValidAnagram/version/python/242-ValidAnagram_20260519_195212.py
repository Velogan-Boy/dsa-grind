# Last updated: 5/19/2026, 7:52:12 PM
1class Solution:
2    def isAnagram(self, s: str, t: str) -> bool:
3        hashMap = defaultdict(int)
4
5        for ch in s:
6            hashMap[ch]+=1
7        
8        for ch in t:
9            hashMap[ch]-=1
10        
11        for k in hashMap.keys():
12            if hashMap[k] != 0: return False
13        
14        return True
15        