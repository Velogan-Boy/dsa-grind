// Last updated: 7/12/2026, 6:25:11 PM
class Solution {
    public int[] searchRange(int[] nums, int target) {
        
        int start = binarySearch(nums,target,true);
        int end = binarySearch(nums,target,false);
        
        int[] ans = new int[2];
        
        ans[0] = start;
        ans[1] = end;
        
        return ans;
        
        
        
    }
    
    int binarySearch(int[] nums, int target, boolean searchFirstOccurence){
        
        int start = 0;
        int end = nums.length - 1;
        int ans = -1;
        
        while(start <= end){
            int mid = start + (end - start) / 2;
            
            if(nums[mid] < target) start = mid + 1;
            else if(nums[mid] > target) end = mid - 1;
            else if(nums[mid] == target) {
                ans = mid;
                
                if(searchFirstOccurence) end = mid - 1;
                else start = mid + 1;
            }
            
            
        }
        
        return ans;
        
    }
}