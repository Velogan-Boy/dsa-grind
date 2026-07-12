# Last updated: 7/12/2026, 6:20:06 PM
import heapq

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        occur = {}
        for num in nums:
            occur[num] = occur.get(num, 0) + 1

        heap = []

        for key in occur:
            heapq.heappush(heap, (occur[key], key))
            if len(heap) > k:
                heapq.heappop(heap)

        return [i[1] for i in heap]