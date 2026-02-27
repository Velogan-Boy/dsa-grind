# Last updated: 2/27/2026, 5:22:52 PM
class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:

        diff = [None] * len(nums)

        for i in range(len(nums)):
            prefixSet = set(nums[:i+1])
            suffixSet = set(nums[i+1:])
            diff[i] = len(prefixSet) - len(suffixSet)

        return diff


        