# Last updated: 4/12/2026, 8:13:08 PM
1class Solution:
2    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
3        count = {}
4        freq = [[] for i in range(len(nums) + 1)]
5
6        for n in nums:
7            count[n] = 1 + count.get(n, 0)
8        for n, c in count.items():
9            freq[c].append(n)
10
11        res = []
12        for i in range(len(freq) - 1, 0, -1):
13            res += freq[i]
14            if len(res) == k:
15                return res
16                
17
18        