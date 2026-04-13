# Last updated: 4/13/2026, 6:01:28 PM
1class Solution:
2    def rob(self, nums: List[int]) -> int:
3        if len(nums) == 1: return nums[0]
4        
5        return max( self.robRec(nums[:-1]) , self.robRec(nums[1:]) )
6
7
8    def robRec(self,nums):
9        prev2 = 0 
10        prev1 = 0 
11
12        for money in nums:
13            curr = max(prev1, prev2 + money)
14            prev2 = prev1
15            prev1 = curr
16
17        return prev1
18        
19        