# Last updated: 7/12/2026, 6:23:52 PM
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        subsets = 1 << n
        ans = []

        for i in range(subsets):
            list = []
            for j in range(n):
                if i & (1 << j):
                    list.append(nums[j])

            ans.append(list)

        return ans


            
        