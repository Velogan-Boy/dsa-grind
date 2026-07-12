# Last updated: 7/12/2026, 6:20:22 PM
import heapq

class MedianFinder:
    def __init__(self):
        self.mx = []
        self.mn = []

    def addNum(self, num):
        if not self.mx or num <= -self.mx[0]:
            heapq.heappush(self.mx, -num)
        else:
            heapq.heappush(self.mn, num)

        if len(self.mx) > len(self.mn) + 1:
            heapq.heappush(self.mn, -heapq.heappop(self.mx))
        elif len(self.mn) > len(self.mx):
            heapq.heappush(self.mx, -heapq.heappop(self.mn))

    def findMedian(self):
        if len(self.mx) == len(self.mn):
            return (-self.mx[0] + self.mn[0]) / 2
        return -self.mx[0]