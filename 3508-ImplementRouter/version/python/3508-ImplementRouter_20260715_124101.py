# Last updated: 7/15/2026, 12:41:01 PM
1from collections import deque, defaultdict
2from bisect import bisect_left, bisect_right, insort
3from sortedcontainers import SortedList
4
5
6class Router:
7
8    def __init__(self, memoryLimit: int):
9        self.memoryLimit = memoryLimit
10
11        self.q = deque()
12        self.seen = set()
13        self.dest = defaultdict(SortedList)
14
15    def addPacket(
16        self,
17        source: int,
18        destination: int,
19        timestamp: int
20    ) -> bool:
21
22        packet = (source, destination, timestamp)
23
24        if packet in self.seen:
25            return False
26
27        if len(self.q) == self.memoryLimit:
28            s, d, t = self.q.popleft()
29            self.seen.remove((s, d, t))
30            self.dest[d].remove(t)
31
32        self.q.append(packet)
33        self.seen.add(packet)
34        self.dest[destination].add(timestamp)
35
36        return True
37
38    def forwardPacket(self) -> list[int]:
39        if not self.q:
40            return []
41
42        s, d, t = self.q.popleft()
43
44        self.seen.remove((s, d, t))
45        self.dest[d].remove(t)
46
47        return [s, d, t]
48
49    def getCount(
50        self,
51        destination: int,
52        startTime: int,
53        endTime: int
54    ) -> int:
55
56        timestamps = self.dest[destination]
57
58        left = timestamps.bisect_left(startTime)
59        right = timestamps.bisect_right(endTime)
60
61        return right - left