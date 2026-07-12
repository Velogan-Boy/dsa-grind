# Last updated: 7/12/2026, 6:22:24 PM
class Solution:
  def singleNumber(self, nums: List[int]) -> int:
    ones = 0
    twos = 0

    for num in nums:
      ones ^= (num & ~twos)
      twos ^= (num & ~ones)

    return ones