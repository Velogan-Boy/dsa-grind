# Last updated: 7/12/2026, 6:17:54 PM
class Solution:
    def numSubarraysWithSum(self, nums, goal):
        
        def func(myGoal):
            if myGoal < 0: return 0

            n = len(nums)
            l, r = 0, 0
            sum = 0
            count = 0

            while r < n:
                sum += nums[r]

                while sum > myGoal:
                    sum-= nums[l]
                    l+=1

                count+= (r - l + 1)
                r+=1


            return count

        return func(goal) - func(goal - 1)