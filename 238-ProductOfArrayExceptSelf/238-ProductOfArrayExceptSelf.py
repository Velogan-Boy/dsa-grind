# Last updated: 2/28/2026, 4:27:44 PM
class Solution:
    def productExceptSelf(self, nums):
        product = math.prod(nums)
        result = []
        if product == 1:
            return nums
        elif product != 0:
            for i in range(len(nums)):
                result.append(product//nums[i])
            return result
        else:
            for i in range(len(nums)):
                result.append(math.prod(nums[:i]+nums[i+1:]))
            return result