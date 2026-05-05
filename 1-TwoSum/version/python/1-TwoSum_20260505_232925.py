# Last updated: 5/5/2026, 11:29:25 PM
1class Solution:
2    def twoSum(self, nums: List[int], target: int) -> List[int]:
3
4        hashMap = {}
5
6        for i in range(len(nums)):
7            if target - nums[i] in hashMap:
8                return [i, hashMap[target - nums[i]]]
9
10            hashMap[nums[i]] = i
11
12        return [-1,-1]
13
14       