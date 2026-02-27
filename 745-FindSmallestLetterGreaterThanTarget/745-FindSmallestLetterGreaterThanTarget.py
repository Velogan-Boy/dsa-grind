# Last updated: 2/27/2026, 9:36:44 PM
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:

        if letters[-1] <= target: return letters[0]

        l, h = 0, len(letters) - 1
        
        while l <= h:
            mid = (l + h )// 2
            if letters[mid] > target:
                h = mid - 1
            else:
                l = mid + 1
        
        return letters[l]