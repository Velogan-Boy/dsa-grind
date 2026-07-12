# Last updated: 7/12/2026, 6:20:37 PM
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        XOR = 0
        
        for i in range(n):
            XOR = XOR ^ nums[i]
        
        rightmost = (XOR & (XOR - 1)) ^ XOR
        
        XOR1, XOR2 = 0, 0
        
        for i in range(n):
            if nums[i] & rightmost:
                XOR1 = XOR1 ^ nums[i]
            else:
                XOR2 = XOR2 ^ nums[i]
        
        return [XOR1, XOR2] if XOR1 < XOR2 else [XOR2, XOR1]

