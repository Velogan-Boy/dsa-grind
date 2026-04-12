# Last updated: 4/12/2026, 6:29:14 PM
1class Solution:
2    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
3            if len(hand) % groupSize != 0:
4                return False
5
6            count = Counter(hand)
7            heap = list(count.keys())
8            heapq.heapify(heap)
9
10            while heap:
11                first = heap[0]
12
13                for i in range(groupSize):
14                    if count[first + i] == 0:
15                        return False
16
17                    count[first + i] -= 1
18
19                    if count[first + i] == 0:
20                        if first + i != heap[0]:
21                            return False
22                        heapq.heappop(heap)
23
24            return True