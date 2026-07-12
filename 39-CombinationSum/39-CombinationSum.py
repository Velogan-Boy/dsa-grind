# Last updated: 7/12/2026, 6:25:03 PM
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        ans = []
        def helper(i, currSum, curr):
            if currSum < 0 or i == len(candidates):
                return
            
            if currSum == 0:
                ans.append(curr[:])
                return
            
            curr.append(candidates[i])
            helper(i, currSum - candidates[i], curr)

            curr.pop()
            helper(i + 1, currSum, curr)


        helper(0, target, [])

        return ans



        