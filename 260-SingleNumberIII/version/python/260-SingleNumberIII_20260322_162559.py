# Last updated: 3/22/2026, 4:25:59 PM
1class Solution:
2    def singleNumber(self, nums: List[int]) -> List[int]:
3        n = len(nums)
4        
5        XOR = 0
6        
7        for i in range(n):
8            XOR = XOR ^ nums[i]
9        
10        rightmost = (XOR & (XOR - 1)) ^ XOR
11        
12        XOR1, XOR2 = 0, 0
13        
14        for i in range(n):
15            if nums[i] & rightmost:
16                XOR1 = XOR1 ^ nums[i]
17            else:
18                XOR2 = XOR2 ^ nums[i]
19        
20        return [XOR1, XOR2] if XOR1 < XOR2 else [XOR2, XOR1]
21
22