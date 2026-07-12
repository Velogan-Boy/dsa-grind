# Last updated: 7/12/2026, 6:25:06 PM
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        n = len(nums)
        l , r = 0, n - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] >= target:
                r = mid - 1
            else:
                l = mid + 1
        
        return l

        