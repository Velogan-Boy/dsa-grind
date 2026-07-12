# Last updated: 7/12/2026, 6:17:32 PM
class Solution:
    def longestOnes(self, nums, k):
        l, r = 0, 0
        n = len(nums)
        ans = 0
        zeroes = 0

        while r < n:
            if nums[r] == 0: zeroes+=1

            while zeroes > k:
                if nums[l] == 0: zeroes-=1
                l+=1

            ans = max(ans, r - l + 1)
            r+=1

        return ans



            
            

                