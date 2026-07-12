# Last updated: 7/12/2026, 6:19:52 PM
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        lowLimit = max(nums)
        upperLimit = sum(nums)

        while lowLimit <= upperLimit:
            maxSum = (lowLimit + upperLimit) // 2
            noOfSubarray = 1
            runningSum = 0

            for num in nums:
                if num + runningSum > maxSum:
                    noOfSubarray+=1
                    runningSum = num
                else:
                    runningSum += num

            if noOfSubarray <= k:
                upperLimit = maxSum - 1
            else:
                lowLimit = maxSum + 1

        return lowLimit

            



        