# Last updated: 5/20/2026, 10:41:44 PM
1class Solution:
2    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
3
4        freq = defaultdict(int)
5
6        for num in nums:
7            freq[num] += 1
8
9        sortedNums = sorted(freq.keys(), key = lambda x: freq[x], reverse=True)
10
11        return sortedNums[:k]
12
13
14
15        
16