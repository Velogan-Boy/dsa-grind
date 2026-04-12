# Last updated: 4/12/2026, 6:16:33 PM
1class Solution:
2    def leastInterval(self, tasks: List[str], n: int) -> int:
3        count = Counter(tasks)
4        maxHeap = [-cnt for cnt in count.values()]
5        heapq.heapify(maxHeap)
6
7        time = 0
8        q = deque()
9        while maxHeap or q:
10            time += 1
11
12            if not maxHeap:
13                time = q[0][1]
14            else:
15                cnt = 1 + heapq.heappop(maxHeap)
16                if cnt:
17                    q.append([cnt, time + n])
18                    
19            if q and q[0][1] == time:
20                heapq.heappush(maxHeap, q.popleft()[0])
21
22        return time
23
24
25# Greedy algorithm
26class Solution(object):
27    def leastInterval(self, tasks: List[str], n: int) -> int:
28        counter = collections.Counter(tasks)
29        max_count = max(counter.values())
30        min_time = (max_count - 1) * (n + 1) + \
31                    sum(map(lambda count: count == max_count, counter.values()))
32    
33        return max(min_time, len(tasks))