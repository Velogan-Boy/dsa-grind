# Last updated: 7/12/2026, 6:23:31 PM
class Solution:
    def func(self, ind, arr, nums, ans):
        if ind == len(nums):
            ans.append(arr.copy())
            return
        
        arr.append(nums[ind])
        self.func(ind + 1, arr, nums, ans)
        arr.pop()
        
        for j in range(ind + 1, len(nums)):
            if nums[j] != nums[ind]:
                self.func(j, arr, nums, ans)
                return
        
        ans.append(arr.copy())
    
    def subsetsWithDup(self, nums):
        ans = [] 
        arr = [] 
        nums.sort()  
        self.func(0, arr, nums, ans)  
        return ans
