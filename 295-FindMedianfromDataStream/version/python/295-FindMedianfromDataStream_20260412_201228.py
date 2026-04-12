# Last updated: 4/12/2026, 8:12:28 PM
1import heapq
2
3class MedianFinder:
4    def __init__(self):
5        self.mx = []
6        self.mn = []
7
8    def addNum(self, num):
9        if not self.mx or num <= -self.mx[0]:
10            heapq.heappush(self.mx, -num)
11        else:
12            heapq.heappush(self.mn, num)
13
14        if len(self.mx) > len(self.mn) + 1:
15            heapq.heappush(self.mn, -heapq.heappop(self.mx))
16        elif len(self.mn) > len(self.mx):
17            heapq.heappush(self.mx, -heapq.heappop(self.mn))
18
19    def findMedian(self):
20        if len(self.mx) == len(self.mn):
21            return (-self.mx[0] + self.mn[0]) / 2
22        return -self.mx[0]