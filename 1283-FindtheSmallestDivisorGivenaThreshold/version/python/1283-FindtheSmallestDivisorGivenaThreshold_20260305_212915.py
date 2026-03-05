# Last updated: 3/5/2026, 9:29:15 PM
1class Solution:
2    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
3        if threshold == 0:
4            return 1
5
6        s = 1
7        e = max(nums)
8
9        while s <= e:
10            x = (s + e) // 2
11
12            sumOfResult = 0
13            for num in nums:
14                sumOfResult += math.ceil(num / x)
15
16            if sumOfResult <= threshold:
17                e = x - 1
18            else:
19                s = x + 1
20
21        return s
22