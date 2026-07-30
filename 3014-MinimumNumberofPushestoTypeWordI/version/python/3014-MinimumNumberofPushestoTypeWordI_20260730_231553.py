# Last updated: 7/30/2026, 11:15:53 PM
1import heapq
2
3class Solution:
4    def minimumPushes(self, word: str) -> int:
5        hashMap = defaultdict(int)
6
7        for ch in word:
8            hashMap[ch] += 1
9        
10        heap = []
11        for key, value in hashMap.items():
12            heapq.heappush(heap, (-value, key))
13
14        ans = 0
15        i = 0
16        while heap:
17            value, key = heapq.heappop(heap)
18            ans += -value * (i // 8 + 1)
19            i += 1
20
21        return ans
22
23        
24        
25
26
27
28        