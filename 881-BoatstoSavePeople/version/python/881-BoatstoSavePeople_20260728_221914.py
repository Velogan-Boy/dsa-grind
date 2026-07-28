# Last updated: 7/28/2026, 10:19:14 PM
1class Solution:
2    def numRescueBoats(self, people: List[int], limit: int) -> int:
3
4        people.sort()
5        n = len(people)
6
7        i, j = 0, n - 1
8
9        boats = 0
10
11        while i <= j:
12            if people[i] + people[j] <= limit:
13                boats += 1
14                i+=1
15                j-=1
16                continue
17            
18            if people[j] > limit: return -1
19
20            j -= 1
21            boats += 1
22
23        return boats
24        
25        return boats