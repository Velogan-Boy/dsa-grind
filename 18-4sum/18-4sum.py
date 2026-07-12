# Last updated: 7/12/2026, 6:25:37 PM
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)

        ans = set()

        for i in range(n):
            if i != 0 and nums[i - 1] == nums[i]: continue

            for j in range(i+1, n):
                if j != i + 1 and  nums[j - 1] == nums[j]: continue

                l = j + 1
                k = n - 1

                while l < k:
                    quadSum = nums[i] + nums[j] + nums[k] + nums[l]

                    if quadSum < target:
                        l+=1
                    elif quadSum > target:
                        k-=1
                    else:
                        ans.add((nums[i],nums[j],nums[l],nums[k]))

                        l+=1
                        k-=1

                        while l < k and nums[l - 1] == nums[l]: l+=1
                        while l < k and nums[k] == nums[k + 1]: k-=1


        return list(ans)




        