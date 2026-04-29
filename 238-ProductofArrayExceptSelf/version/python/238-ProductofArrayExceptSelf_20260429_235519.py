# Last updated: 4/29/2026, 11:55:19 PM
1class Solution:
2    def productExceptSelf(self, nums: List[int]) -> List[int]:
3        product = math.prod(nums)
4        result = []
5        if product == 1:
6            return nums
7        elif product != 0:
8            for i in range(len(nums)):
9                result.append(product//nums[i])
10            return result
11        else:
12            for i in range(len(nums)):
13                result.append(math.prod(nums[:i]+nums[i+1:]))
14            return result