# Last updated: 2/28/2026, 4:28:00 PM
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        
        return max( self.robRec(nums[:-1]) , self.robRec(nums[1:]) )


    def robRec(self,nums):
        prev2 = 0 
        prev1 = 0 

        for money in nums:
            curr = max(prev1, prev2 + money)
            prev2 = prev1
            prev1 = curr

        return prev1
        
        