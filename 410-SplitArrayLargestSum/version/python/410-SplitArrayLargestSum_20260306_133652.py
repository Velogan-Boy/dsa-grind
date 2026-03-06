# Last updated: 3/6/2026, 1:36:52 PM
1class Solution:
2    def splitArray(self, nums: List[int], k: int) -> int:
3        lowLimit = max(nums)
4        upperLimit = sum(nums)
5
6        while lowLimit <= upperLimit:
7            maxSum = (lowLimit + upperLimit) // 2
8            noOfSubarray = 1
9            runningSum = 0
10
11            for num in nums:
12                if num + runningSum > maxSum:
13                    noOfSubarray+=1
14                    runningSum = num
15                else:
16                    runningSum += num
17
18            if noOfSubarray <= k:
19                upperLimit = maxSum - 1
20            else:
21                lowLimit = maxSum + 1
22
23        return lowLimit
24
25            
26
27
28
29        