// Last updated: 2/27/2026, 5:12:11 PM
class Solution {
    public int searchInsert(int[] nums, int target) {
        
        int i = 0;
        int j = nums.length - 1;
        int mid = i + ( j - i ) / 2;

        while(i <= j){

            if(target == nums[mid]) return mid;

            else if(target < nums[mid]) j = mid - 1;
            else if(target > nums[mid]) i = mid + 1;

            mid = i + (j - i) / 2;
        }

        return j + 1;
        


    }
}