# Last updated: 3/18/2026, 4:37:33 PM
1class Solution:
2    def func(self, ind, arr, nums, ans):
3        if ind == len(nums):
4            ans.append(arr.copy())
5            return
6        
7        arr.append(nums[ind])
8        self.func(ind + 1, arr, nums, ans)
9        arr.pop()
10        
11        for j in range(ind + 1, len(nums)):
12            if nums[j] != nums[ind]:
13                self.func(j, arr, nums, ans)
14                return
15        
16        self.func(len(nums), arr, nums, ans)
17    
18    def subsetsWithDup(self, nums):
19        ans = [] 
20        arr = [] 
21        nums.sort()  
22        self.func(0, arr, nums, ans)  
23        return ans
24