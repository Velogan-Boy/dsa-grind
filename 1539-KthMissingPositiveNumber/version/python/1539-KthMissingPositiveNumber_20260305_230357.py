# Last updated: 3/5/2026, 11:03:57 PM
1class Solution:
2    def findKthPositive(self, arr: List[int], k: int) -> int:
3
4        hashSet = set(arr)
5
6        curr = 0
7        for x in range(1, max(arr) + k + 1):
8            if x not in hashSet:
9                curr+=1
10            
11            if curr == k: return x
12                
13        return max(arr) + k + 1
14        