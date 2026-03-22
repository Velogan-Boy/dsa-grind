# Last updated: 3/22/2026, 4:20:07 PM
1class Solution:
2  def singleNumber(self, nums: List[int]) -> int:
3    ones = 0
4    twos = 0
5
6    for num in nums:
7      ones ^= (num & ~twos)
8      twos ^= (num & ~ones)
9
10    return ones