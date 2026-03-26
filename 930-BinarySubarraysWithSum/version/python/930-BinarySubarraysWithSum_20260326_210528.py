# Last updated: 3/26/2026, 9:05:28 PM
1class Solution:
2    def numSubarraysWithSum(self, nums, goal):
3        
4        def func(myGoal):
5            if myGoal < 0: return 0
6
7            n = len(nums)
8            l, r = 0, 0
9            sum = 0
10            count = 0
11
12            while r < n:
13                sum += nums[r]
14
15                while sum > myGoal:
16                    sum-= nums[l]
17                    l+=1
18
19                count+= (r - l + 1)
20                r+=1
21
22
23            return count
24
25        return func(goal) - func(goal - 1)