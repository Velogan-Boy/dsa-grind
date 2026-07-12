# Last updated: 7/12/2026, 6:19:50 PM
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)
        if totalSum % 2 != 0: return False
        n = len(nums)

        target = totalSum // 2

        prev = [False] * (target + 1) 
        prev[0] = True

        if nums[0] <= target:
            prev[nums[0]] = True
        
        for i in range(1, n):
            curr = [False] * (target + 1)
            curr[0] = True

            for j in range(1, target + 1):
                notPick = prev[j]

                pick = False
                if nums[i] <= j:
                    pick = prev[j - nums[i]]

                curr[j] = pick or notPick
            
            prev = curr


        return prev[target]
