# Last updated: 5/18/2026, 5:55:14 PM
1class Solution:
2    def findMiddleIndex(self, nums: List[int]) -> int:
3        n = len(nums)
4        prefixSum = [0] * n
5
6        for i in range(1, n):
7            prefixSum[i] = prefixSum[i - 1] + nums[i - 1]
8        
9        runningSum = 0
10        ans = -1
11        for i in range(n - 1, -1, -1):
12            if runningSum == prefixSum[i]:
13                ans = i
14            
15            runningSum += nums[i]
16        
17        return ans
18
19
20
21        