# Last updated: 7/7/2026, 12:04:12 AM
1import heapq
2
3class Solution:
4    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
5        occur = {}
6        for num in nums:
7            occur[num] = occur.get(num, 0) + 1
8
9        heap = []
10
11        for key in occur:
12            heapq.heappush(heap, (occur[key], key))
13            if len(heap) > k:
14                heapq.heappop(heap)
15
16        return [i[1] for i in heap]