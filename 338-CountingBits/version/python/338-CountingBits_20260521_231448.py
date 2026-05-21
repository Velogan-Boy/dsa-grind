# Last updated: 5/21/2026, 11:14:48 PM
1class Solution:
2    def countBits(self, n: int) -> List[int]:
3
4        arr = [0] * (n + 1)
5
6        for i in range(n + 1):
7            num = i
8
9            # find number of set bits
10            count = 0
11
12            while num:
13                num = num & (num - 1)
14                count += 1
15            
16            arr[i] = count
17        
18        return arr
19
20        
21
22        