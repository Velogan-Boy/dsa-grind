# Last updated: 3/5/2026, 9:53:53 PM
1class Solution:
2    def shipWithinDays(self, weights: List[int], days: int) -> int:
3        s = max(weights)
4        e = sum(weights)
5        
6        while s <= e:
7            capacity = (s + e) // 2
8
9            actualDays = 0
10            totalWeight = 0
11            for weight in weights:
12                if totalWeight + weight > capacity:
13                    actualDays+=1
14                    totalWeight = weight
15                else:
16                    totalWeight += weight
17            
18            if totalWeight != 0: actualDays+=1
19
20            if actualDays <= days: 
21                e = capacity - 1
22            else:
23                s = capacity + 1
24
25        return s
26
27
28