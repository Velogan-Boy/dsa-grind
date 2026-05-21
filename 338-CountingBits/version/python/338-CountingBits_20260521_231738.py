# Last updated: 5/21/2026, 11:17:38 PM
1class Solution:
2    def countBits(self, n: int) -> List[int]:
3
4        counter = [0]
5
6        for i in range(1, n+1):
7            counter.append(counter[i // 2] + i % 2)
8            
9        return counter
10
11            
12
13        