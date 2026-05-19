# Last updated: 5/19/2026, 6:19:25 PM
1class Solution:
2    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
3        if sum(gas) < sum(cost):
4            return -1
5        
6        start = 0
7        tank = 0
8        for i in range(len(gas)):
9            tank += gas[i] - cost[i]
10
11            if tank < 0:
12                tank = 0
13                start = i + 1
14            
15        return start
16
17
18