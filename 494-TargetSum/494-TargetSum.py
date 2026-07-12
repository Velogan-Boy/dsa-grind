# Last updated: 7/12/2026, 6:19:31 PM
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)

        if (target + total) % 2 != 0 or abs(target) > total:
            return 0

        P = (target + total) // 2
        n = len(nums)

        memo = {}

        def dfs(i, curr_sum):
            if i == 0:
                if curr_sum == 0 and nums[0] == 0:
                    return 2  # +0 and -0
                if curr_sum == 0 or curr_sum == nums[0]:
                    return 1
                return 0

            if (i, curr_sum) in memo:
                return memo[(i, curr_sum)]

            not_take = dfs(i - 1, curr_sum)
            take = 0
            if nums[i] <= curr_sum:
                take = dfs(i - 1, curr_sum - nums[i])

            memo[(i, curr_sum)] = take + not_take
            return memo[(i, curr_sum)]

        return dfs(n - 1, P)