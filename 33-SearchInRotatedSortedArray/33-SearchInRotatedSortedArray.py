# Last updated: 7/12/2026, 6:25:09 PM
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        n = len(nums)
        s, e = 0, n - 1

        while s <= e:
            mid = (s + e) // 2

            if nums[mid] == target: return mid

            if nums[s] <= nums[mid]:
                if nums[s] <= target <= nums[mid]:
                    e = mid - 1
                else:
                    s = mid + 1
            else:
                if nums[mid] <= target <= nums[e]:
                    s = mid + 1
                else:
                    e = mid - 1
        
        return -1
                
                


     

