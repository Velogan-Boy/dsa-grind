# Last updated: 3/1/2026, 11:12:48 AM
1class Solution:
2    def majorityElement(self, nums: List[int]) -> List[int]:
3        count = Counter(nums)
4        n = len(nums)
5
6        ansSet = set()
7        for num in nums:
8            if count[num] > n // 3:
9                ansSet.add(num)
10
11        return list(ansSet)
12
13        