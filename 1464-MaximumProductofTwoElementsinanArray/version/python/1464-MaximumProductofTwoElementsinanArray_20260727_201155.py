# Last updated: 7/27/2026, 8:11:55 PM
1class Solution:
2    def maxProduct(self, nums: List[int]) -> int:
3
4        n = len(nums)
5        maxValue = 0
6        sMaxValue = 0
7
8        for num in nums:
9            if num > maxValue:
10                sMaxValue = maxValue
11                maxValue = num
12            
13            elif num > sMaxValue:
14                sMaxValue = num
15            
16        return (maxValue - 1) * (sMaxValue - 1)
17
18
19
20
21
22        
23
24        