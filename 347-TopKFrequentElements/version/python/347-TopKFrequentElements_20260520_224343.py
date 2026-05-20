# Last updated: 5/20/2026, 10:43:43 PM
1from collections import defaultdict
2from typing import List
3
4class Solution:
5    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
6        freq = defaultdict(int)
7        for num in nums:
8            freq[num] += 1
9
10        buckets = [[] for _ in range(len(nums) + 1)]
11
12        for num, count in freq.items():
13            buckets[count].append(num)
14
15        result = []
16
17        for count in range(len(nums), 0, -1):
18            for num in buckets[count]:
19                result.append(num)
20                if len(result) == k:
21                    return result