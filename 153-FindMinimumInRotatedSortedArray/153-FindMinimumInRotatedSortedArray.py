# Last updated: 7/12/2026, 6:21:57 PM
class Solution:
    def findMin(self, nums: List[int]) -> int:
        s = 0
        e = len(nums) - 1
        ans = inf

        while s <= e:
            mid = (s + e) // 2

            if nums[s] <= nums[mid]:
                ans = min(ans,nums[s])
                s = mid + 1
            else:
                ans = min(ans,nums[mid])
                e = mid - 1
        
        return ans if ans != inf else -1


        