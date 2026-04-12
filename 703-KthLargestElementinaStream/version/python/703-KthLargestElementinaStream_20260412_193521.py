# Last updated: 4/12/2026, 7:35:21 PM
1class KthLargest:
2
3    def __init__(self, k, nums):
4        self.K = k 
5        self.pq = [] 
6
7        for num in nums:
8            if len(self.pq) < self.K:
9                heapq.heappush(self.pq, num)  
10            elif num > self.pq[0]:
11                heapq.heappop(self.pq)  
12                heapq.heappush(self.pq, num)  
13
14
15    def add(self, val):
16        if len(self.pq) < self.K:
17            heapq.heappush(self.pq, val)
18
19            return self.pq[0]
20
21        if val > self.pq[0]:
22            heapq.heappop(self.pq)
23            heapq.heappush(self.pq, val)  
24
25        return self.pq[0]  
26
27
28
29