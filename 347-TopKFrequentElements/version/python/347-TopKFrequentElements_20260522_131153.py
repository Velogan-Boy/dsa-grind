# Last updated: 5/22/2026, 1:11:53 PM
1import heapq
2
3class Solution:
4    """My Own Min-Heap Solution!!!"""
5    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
6        occur = {}
7        for num in nums:
8            occur[num] = occur.get(num, 0) + 1
9
10        heap = []
11
12        for key in occur:
13            heapq.heappush(heap, (occur[key], key))
14            if len(heap) > k:
15                heapq.heappop(heap)
16
17        return [i[1] for i in heap]