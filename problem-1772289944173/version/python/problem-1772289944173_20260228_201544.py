# Last updated: 2/28/2026, 8:15:44 PM
1class Solution:
2    def minDistinctFreqPair(self, nums: list[int]) -> list[int]:
3
4        hashMap = {}
5
6        for num in nums:
7            if num in hashMap:
8                hashMap[num] += 1
9            else:
10                hashMap[num] = 1
11
12        nums.sort()
13
14        for i in range(len(nums)):
15            for j in range(i + 1, len(nums)):
16                if nums[i] < nums[j] and hashMap[nums[i]] != hashMap[nums[j]]:
17                    return [nums[i],nums[j]]
18
19        return [-1, -1]
20
21        #sort the array -> take the first two, slide if not applied
22        