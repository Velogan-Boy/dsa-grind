# Last updated: 2/28/2026, 10:14:26 PM
class Solution:
    def minDistinctFreqPair(self, nums: list[int]) -> list[int]:

        hashMap = {}

        for num in nums:
            if num in hashMap:
                hashMap[num] += 1
            else:
                hashMap[num] = 1

        nums.sort()

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j] and hashMap[nums[i]] != hashMap[nums[j]]:
                    return [nums[i],nums[j]]

        return [-1, -1]

        #sort the array -> take the first two, slide if not applied
        