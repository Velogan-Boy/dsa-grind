# Last updated: 7/12/2026, 6:18:17 PM
class KthLargest:

    def __init__(self, k, nums):
        self.K = k 
        self.pq = [] 

        for num in nums:
            if len(self.pq) < self.K:
                heapq.heappush(self.pq, num)  
            elif num > self.pq[0]:
                heapq.heappop(self.pq)  
                heapq.heappush(self.pq, num)  


    def add(self, val):
        if len(self.pq) < self.K:
            heapq.heappush(self.pq, val)

            return self.pq[0]

        if val > self.pq[0]:
            heapq.heappop(self.pq)
            heapq.heappush(self.pq, val)  

        return self.pq[0]  



