# Last updated: 7/12/2026, 6:24:31 PM
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxIndex = 0

        for i in range(len(nums)):
            if i > maxIndex: return False
            maxIndex = max(i + nums[i], maxIndex)


        return True

        