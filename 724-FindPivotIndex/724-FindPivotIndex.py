# Last updated: 7/12/2026, 6:18:40 PM
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)

        totalSum = sum(nums)
        leftSum = 0

        for i in range(n):
            if leftSum * 2 == totalSum - nums[i]:
                return i
            
            leftSum += nums[i]

        return -1



        