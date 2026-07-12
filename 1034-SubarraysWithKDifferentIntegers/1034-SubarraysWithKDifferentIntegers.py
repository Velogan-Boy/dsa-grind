# Last updated: 7/12/2026, 6:17:43 PM
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def kDistinctChar(myK):
            if myK < 0: return 0

            l,r = 0,0 
            n = len(nums)
            hm = {}
            count = 0

            while r < n:
                hm[nums[r]] = hm.get(nums[r], 0) + 1

                while len(hm) > myK:
                    hm[nums[l]] -= 1
                    if hm[nums[l]] == 0: del hm[nums[l]]
                    l += 1

                count += r - l + 1
                r+= 1
            
            return count

        return  kDistinctChar(k) - kDistinctChar(k - 1) 

    
        