# Last updated: 2/27/2026, 5:21:23 PM
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:

        pos, neg = [], []

        for i in range(len(nums)):
            if nums[i] < 0:
                neg.append(nums[i])
            else:
                pos.append(nums[i])

        i,j,k = 0,0,0

        while i < len(nums):
            if i % 2 == 0:
                nums[i] = pos[j]
                j+=1
            else:
                nums[i] = neg[k]
                k+=1
            
            i+=1

        return nums

        