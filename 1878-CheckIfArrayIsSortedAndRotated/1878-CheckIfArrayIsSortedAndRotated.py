# Last updated: 2/27/2026, 5:21:26 PM
class Solution:
    def check(self, nums: List[int]) -> bool:
        cnt = 0

        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                cnt+=1
        
        if nums[-1] > nums[0]:
            cnt+=1

        return cnt <= 1