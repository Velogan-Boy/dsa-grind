# Last updated: 4/28/2026, 10:59:52 PM
1class Solution:
2    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
3        empty = 0
4        f = [0] + flowerbed + [0]
5
6        for i in range(1, len(f) - 1):
7            if f[i] == 1: continue
8
9            if f[i - 1] == 0 and f[i + 1] == 0:
10                empty+=1
11                f[i] = 1
12
13        return empty >= n
14        
15
16
17        