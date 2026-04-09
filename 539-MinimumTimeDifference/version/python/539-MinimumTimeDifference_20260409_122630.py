# Last updated: 4/9/2026, 12:26:30 PM
1class Solution:
2    def findMinDifference(self, timePoints: List[str]) -> int:
3        def timeToMinutes(time: str) -> int:
4            hours, minutes = map(int, time.split(':'))
5            return hours * 60 + minutes
6        
7        minutes = [timeToMinutes(tp) for tp in timePoints]
8        
9        minutes.sort()
10        
11        min_diff = float('inf')  # Initialize to a large number
12        
13        for i in range(1, len(minutes)):
14            min_diff = min(min_diff, minutes[i] - minutes[i - 1])
15        
16        circular_diff = 1440 - minutes[-1] + minutes[0]
17        min_diff = min(min_diff, circular_diff)
18        
19        return min_diff