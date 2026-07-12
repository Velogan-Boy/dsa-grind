# Last updated: 7/12/2026, 6:25:07 PM
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        s = self.binarySearch(nums,target, True)
        e = self.binarySearch(nums,target, False)

        return [s, e]

    def binarySearch(self, nums: List[int], target: int, firstOccurence: bool) -> int:
        l, h = 0, len(nums)-1
        ans = -1

        while l <= h:
            mid = (l + h) // 2
            if nums[mid] > target: h = mid - 1
            elif nums[mid] < target: l = mid + 1
            else:
                ans = mid

                if firstOccurence: h = mid - 1
                else: l = mid + 1

                

        
        return ans


        