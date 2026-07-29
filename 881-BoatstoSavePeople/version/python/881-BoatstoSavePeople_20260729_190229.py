# Last updated: 7/29/2026, 7:02:29 PM
1class Solution:
2    def numRescueBoats(self, people: List[int], limit: int) -> int:
3        people.sort()
4
5        i, j = 0, len(people) - 1
6        boats = 0
7
8        while i <= j:
9            if people[i] + people[j] <= limit:
10                i += 1
11            j -= 1
12            boats += 1
13
14        return boats