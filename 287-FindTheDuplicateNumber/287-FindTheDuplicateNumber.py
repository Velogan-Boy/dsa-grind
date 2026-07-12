# Last updated: 7/12/2026, 6:20:29 PM
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        for i in range(len(nums)):
            idx = abs(nums[i])
            if nums[idx] < 0:
                return idx

            nums[idx] = -nums[idx] 

        return 0
        