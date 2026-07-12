// Last updated: 7/12/2026, 6:23:49 PM
class Solution {
	public static boolean search(int[] nums, int target) {
        
        int s = 0;
        int e = nums.length -1;
        
        while(s<=e){
            int mid = s + (e - s) / 2;
            
            if(nums[mid] == target) return true;
            
            // if left side is sorted
            if (nums[mid] > nums[s]) {
                if(target >= nums[s] && target <= nums[mid]){
                    e = mid;
                }else s = mid + 1;
                
            }
            
            // if right side is sorted
            else if(nums[mid] < nums[s]){
                if(target >= nums[mid] && target <= nums[e]){
                    s = mid;
                } else e = mid - 1;
            } else {
                // if nums[s] == nums[e] == nums[mid]
                s++;
            }
        }
        
        return false;
        
        
    }
}