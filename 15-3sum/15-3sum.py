# Last updated: 2/27/2026, 5:22:39 PM
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and nums[i - 1] == a: continue

            if a > 0: break

            left = i + 1
            right = len(nums) - 1

            while left < right:
                currSum = a + nums[left] + nums[right]

                if currSum < 0: left+=1
                elif currSum > 0: right-=1
                else:
                    res.append([a,nums[left],nums[right]])
                    left +=1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right: left += 1
                    while nums[right] == nums[right + 1] and left < right: right -= 1 

        return  res
                










        
