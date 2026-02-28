// Last updated: 2/28/2026, 4:26:37 PM
class Solution {
    public int search(int[] nums, int target) {
        
        int s = 0;
        int e = nums.length - 1;
        int mid;

        while(s <= e){
            mid = s + (e - s) / 2;

            if(nums[mid] == target) return mid;
            else if(nums[mid] < target) s = mid + 1;
            else e = mid - 1;
            

        }

        return -1;
    }
}